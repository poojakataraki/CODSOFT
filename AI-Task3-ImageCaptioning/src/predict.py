from __future__ import annotations

import argparse
from pathlib import Path

from src.captioner import ImageCaptioner
from src.image_utils import load_image


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate a caption for one image.")
    parser.add_argument("image", help="Path to an image file.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    image_path = Path(args.image)

    if not image_path.exists():
        raise FileNotFoundError(f"Image not found: {image_path}")

    captioner = ImageCaptioner()
    image = load_image(image_path)
    print(captioner.generate_caption(image))


if __name__ == "__main__":
    main()
