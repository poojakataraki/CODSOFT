from __future__ import annotations

import argparse
from pathlib import Path

import torch
from torch import nn
from torch.utils.data import DataLoader
from tqdm import tqdm

from src.dataset import CaptionDataset, caption_collate_fn
from src.model import ImageCaptioningModel


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Train a ResNet + LSTM image captioning model.")
    parser.add_argument("--image-dir", required=True, help="Directory containing training images.")
    parser.add_argument("--captions", required=True, help="CSV file with image and caption columns.")
    parser.add_argument("--epochs", type=int, default=5)
    parser.add_argument("--batch-size", type=int, default=32)
    parser.add_argument("--learning-rate", type=float, default=3e-4)
    parser.add_argument("--min-freq", type=int, default=2)
    parser.add_argument("--checkpoint-dir", default="checkpoints")
    return parser.parse_args()


def train() -> None:
    args = parse_args()
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    dataset = CaptionDataset(
        image_dir=args.image_dir,
        captions_file=args.captions,
        min_freq=args.min_freq,
    )
    loader = DataLoader(
        dataset,
        batch_size=args.batch_size,
        shuffle=True,
        num_workers=0,
        collate_fn=caption_collate_fn,
    )

    model = ImageCaptioningModel(vocab_size=len(dataset.vocabulary)).to(device)
    criterion = nn.CrossEntropyLoss(ignore_index=dataset.vocabulary.pad_idx)
    optimizer = torch.optim.AdamW(model.parameters(), lr=args.learning_rate)

    checkpoint_dir = Path(args.checkpoint_dir)
    checkpoint_dir.mkdir(parents=True, exist_ok=True)

    for epoch in range(1, args.epochs + 1):
        model.train()
        total_loss = 0.0

        progress = tqdm(loader, desc=f"Epoch {epoch}/{args.epochs}")
        for images, captions in progress:
            images = images.to(device)
            captions = captions.to(device)

            outputs = model(images, captions)
            targets = captions

            loss = criterion(
                outputs.reshape(-1, outputs.size(-1)),
                targets.reshape(-1),
            )

            optimizer.zero_grad()
            loss.backward()
            optimizer.step()

            total_loss += loss.item()
            progress.set_postfix(loss=f"{loss.item():.4f}")

        average_loss = total_loss / max(len(loader), 1)
        checkpoint_path = checkpoint_dir / f"resnet_lstm_epoch_{epoch}.pt"
        torch.save(
            {
                "epoch": epoch,
                "model_state_dict": model.state_dict(),
                "optimizer_state_dict": optimizer.state_dict(),
                "vocabulary": dataset.vocabulary.token_to_idx,
                "loss": average_loss,
            },
            checkpoint_path,
        )
        print(f"Epoch {epoch}: loss={average_loss:.4f}, saved={checkpoint_path}")


if __name__ == "__main__":
    train()
