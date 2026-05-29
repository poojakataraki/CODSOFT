from __future__ import annotations

import re
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

import pandas as pd
import torch
from PIL import Image
from torch.nn.utils.rnn import pad_sequence
from torch.utils.data import Dataset
from torchvision import transforms


TOKEN_PATTERN = re.compile(r"[a-z]+(?:'[a-z]+)?")


def tokenize(text: str) -> list[str]:
    return TOKEN_PATTERN.findall(text.lower())


@dataclass
class Vocabulary:
    token_to_idx: dict[str, int]

    @classmethod
    def build(cls, captions: list[str], min_freq: int = 2) -> "Vocabulary":
        counter: Counter[str] = Counter()
        for caption in captions:
            counter.update(tokenize(caption))

        token_to_idx = {
            "<pad>": 0,
            "<start>": 1,
            "<end>": 2,
            "<unk>": 3,
        }

        for token, count in counter.items():
            if count >= min_freq:
                token_to_idx[token] = len(token_to_idx)

        return cls(token_to_idx=token_to_idx)

    @property
    def pad_idx(self) -> int:
        return self.token_to_idx["<pad>"]

    def __len__(self) -> int:
        return len(self.token_to_idx)

    def encode(self, caption: str) -> list[int]:
        ids = [self.token_to_idx["<start>"]]
        ids.extend(
            self.token_to_idx.get(token, self.token_to_idx["<unk>"])
            for token in tokenize(caption)
        )
        ids.append(self.token_to_idx["<end>"])
        return ids


class CaptionDataset(Dataset):
    def __init__(
        self,
        image_dir: str | Path,
        captions_file: str | Path,
        vocabulary: Vocabulary | None = None,
        min_freq: int = 2,
    ) -> None:
        self.image_dir = Path(image_dir)
        self.data = pd.read_csv(captions_file)

        if not {"image", "caption"}.issubset(self.data.columns):
            raise ValueError("Captions CSV must contain 'image' and 'caption' columns.")

        captions = self.data["caption"].astype(str).tolist()
        self.vocabulary = vocabulary or Vocabulary.build(captions, min_freq=min_freq)

        self.transform = transforms.Compose(
            [
                transforms.Resize((224, 224)),
                transforms.ToTensor(),
                transforms.Normalize(
                    mean=[0.485, 0.456, 0.406],
                    std=[0.229, 0.224, 0.225],
                ),
            ]
        )

    def __len__(self) -> int:
        return len(self.data)

    def __getitem__(self, index: int) -> tuple[torch.Tensor, torch.Tensor]:
        row = self.data.iloc[index]
        image_path = self.image_dir / str(row["image"])
        caption = str(row["caption"])

        image = Image.open(image_path).convert("RGB")
        image_tensor = self.transform(image)
        caption_tensor = torch.tensor(self.vocabulary.encode(caption), dtype=torch.long)

        return image_tensor, caption_tensor


def caption_collate_fn(
    batch: list[tuple[torch.Tensor, torch.Tensor]],
) -> tuple[torch.Tensor, torch.Tensor]:
    images, captions = zip(*batch)
    image_batch = torch.stack(images)
    caption_batch = pad_sequence(captions, batch_first=True, padding_value=0)
    return image_batch, caption_batch
