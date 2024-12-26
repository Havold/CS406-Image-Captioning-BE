from transformers import (
    MT5ForConditionalGeneration,
    MT5Tokenizer,
    CLIPModel,
    PreTrainedModel,
    PretrainedConfig,
)
import torch
import torch.nn as nn

def freeze_model_layers(model):
    """
    Completely prevent any layer from being updated
    """
    for param in model.parameters():
        param.requires_grad = False


class CLIPMT5ImageCaptioningConfig(PretrainedConfig):
    model_type = "image_captioning"

    def __init__(
        self,
        clip_model_name="openai/clip-vit-base-patch32",
        mt5_model_name="google/mt5-small",
        max_caption_length=192 ,
        **kwargs,
    ):
        super().__init__(**kwargs)
        self.clip_model_name = clip_model_name
        self.mt5_model_name = mt5_model_name
        self.max_caption_length = max_caption_length


class CLIPMT5ImageCaptioningModel(PreTrainedModel):
    config_class = CLIPMT5ImageCaptioningConfig

    def __init__(self, config):
        super().__init__(config)
        self.clip = CLIPModel.from_pretrained(config.clip_model_name)
        self.mt5 = MT5ForConditionalGeneration.from_pretrained(config.mt5_model_name)
        self.tokenizer = MT5Tokenizer.from_pretrained(config.mt5_model_name)

        clip_output_dim = self.clip.config.projection_dim
        mt5_input_dim = self.mt5.config.d_model
        self.projection = nn.Linear(clip_output_dim, mt5_input_dim)

        # Freeze CLIP
        freeze_model_layers(self.clip)

    def forward(self, images, captions):
        # Encode images using CLIP
        image_features = self.clip.get_image_features(images)
        image_embeddings = self.projection(image_features)

        # Prepare inputs for MT5
        outputs = self.mt5(
            inputs_embeds=image_embeddings.unsqueeze(1),
            labels=captions,
        )
        return {
            "loss": outputs.loss,
        }

    def generate(self, images):
        with torch.no_grad():
            image_features = self.clip.get_image_features(images)
            image_embeddings = self.projection(image_features)
            outputs = self.mt5.generate(max_length=90, inputs_embeds=image_embeddings.unsqueeze(1))
            return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)