from pathlib import Path
from typing import BinaryIO

from PIL import Image


def load_image(source: str | Path | BinaryIO) -> Image.Image:
    """Load an image and normalize it to RGB."""
    image = Image.open(source)
    return image.convert("RGB")
