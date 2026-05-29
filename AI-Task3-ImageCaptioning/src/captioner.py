from dataclasses import dataclass

import torch
from PIL import Image
from transformers import BlipForConditionalGeneration, BlipProcessor


@dataclass
class CaptionConfig:
    model_name: str = "Salesforce/blip-image-captioning-base"
    max_new_tokens: int = 40
    num_beams: int = 5


class ImageCaptioner:
    """Small wrapper around a pretrained image captioning transformer."""

    def __init__(self, config: CaptionConfig | None = None) -> None:
        self.config = config or CaptionConfig()
        self.device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

        self.processor = BlipProcessor.from_pretrained(self.config.model_name)
        self.model = BlipForConditionalGeneration.from_pretrained(
            self.config.model_name
        ).to(self.device)
        self.model.eval()

    @torch.inference_mode()
    def generate_caption(self, image: Image.Image) -> str:
        inputs = self.processor(images=image, return_tensors="pt").to(self.device)

        output_ids = self.model.generate(
            **inputs,
            max_new_tokens=self.config.max_new_tokens,
            num_beams=self.config.num_beams,
        )

        caption = self.processor.decode(output_ids[0], skip_special_tokens=True)
        return caption.strip().capitalize()
