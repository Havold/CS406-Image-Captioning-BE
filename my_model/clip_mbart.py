from transformers import (
    MBart50TokenizerFast,
    MBartForConditionalGeneration,
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

class CLIPMBartImageCaptioningConfig(PretrainedConfig):
    model_type = "image_captioning"
    
    def __init__(self, clip_model_name="openai/clip-vit-base-patch32", mbart_model_name="facebook/mbart-large-50-many-to-many-mmt", max_caption_length=140, **kwargs):
        super().__init__(**kwargs)
        self.clip_model_name = clip_model_name
        self.mbart_model_name = mbart_model_name
        self.max_caption_length = max_caption_length
        
class CLIPMBartImageCaptioningModel(PreTrainedModel):
    config_class = CLIPMBartImageCaptioningConfig
    def __init__(self, config):
        super().__init__(config)
        self.clip = CLIPModel.from_pretrained(config.clip_model_name)
        #self.clip_preprocess = CLIPProcessor.from_pretrained(config.clip_model_name)
        self.mbart = MBartForConditionalGeneration.from_pretrained(config.mbart_model_name)
        self.tokenizer = MBart50TokenizerFast.from_pretrained(config.mt5_model_name)
        self.tokenizer.src_lang = "vi_VN"
        self.tokenizer.tgt_lang = "vi_VN"
        clip_output_dim = self.clip.config.projection_dim
        mbart_input_dim = self.mbart.config.d_model
        self.projection = nn.Linear(clip_output_dim, mbart_input_dim)

        # Freeze CLIP
        freeze_model_layers(self.clip)

    def forward(self, images, captions):
        # Encode images using CLIP
        image_features = self.clip.get_image_features(images)
        image_embeddings = self.projection(image_features)
        
        # Prepare inputs for MT5
        # labels = self.tokenizer(captions, return_tensors="pt", padding=True, truncation=True, max_length=self.config.max_caption_length)
        outputs = self.mbart(
            inputs_embeds=image_embeddings.unsqueeze(1),
            labels=captions,
        )

        return {
            "loss": outputs.loss,
            # "logits": outputs.logits,
            #outputs
        }
    def generate(self, images):
        with torch.no_grad():
            image_features = self.clip.get_image_features(images)
            image_embeddings = self.projection(image_features)
            outputs = self.mbart.generate(inputs_embeds=image_embeddings.unsqueeze(1))
        return self.tokenizer.batch_decode(outputs, skip_special_tokens=True)