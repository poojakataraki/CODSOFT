from __future__ import annotations

import torch
from torch import nn
from torchvision.models import ResNet50_Weights, resnet50


class EncoderCNN(nn.Module):
    def __init__(self, embed_size: int, train_backbone: bool = False) -> None:
        super().__init__()
        backbone = resnet50(weights=ResNet50_Weights.DEFAULT)
        modules = list(backbone.children())[:-1]
        self.backbone = nn.Sequential(*modules)

        for parameter in self.backbone.parameters():
            parameter.requires_grad = train_backbone

        self.projection = nn.Linear(backbone.fc.in_features, embed_size)
        self.batch_norm = nn.BatchNorm1d(embed_size, momentum=0.01)

    def forward(self, images: torch.Tensor) -> torch.Tensor:
        with torch.set_grad_enabled(any(p.requires_grad for p in self.backbone.parameters())):
            features = self.backbone(images).flatten(1)

        features = self.projection(features)
        return self.batch_norm(features)


class DecoderRNN(nn.Module):
    def __init__(
        self,
        embed_size: int,
        hidden_size: int,
        vocab_size: int,
        num_layers: int = 1,
        dropout: float = 0.2,
    ) -> None:
        super().__init__()
        self.embedding = nn.Embedding(vocab_size, embed_size)
        self.lstm = nn.LSTM(
            embed_size,
            hidden_size,
            num_layers=num_layers,
            batch_first=True,
            dropout=dropout if num_layers > 1 else 0.0,
        )
        self.fc = nn.Linear(hidden_size, vocab_size)

    def forward(self, image_features: torch.Tensor, captions: torch.Tensor) -> torch.Tensor:
        embeddings = self.embedding(captions[:, :-1])
        inputs = torch.cat((image_features.unsqueeze(1), embeddings), dim=1)
        hidden_states, _ = self.lstm(inputs)
        return self.fc(hidden_states)


class ImageCaptioningModel(nn.Module):
    def __init__(
        self,
        vocab_size: int,
        embed_size: int = 256,
        hidden_size: int = 512,
        num_layers: int = 1,
    ) -> None:
        super().__init__()
        self.encoder = EncoderCNN(embed_size=embed_size)
        self.decoder = DecoderRNN(
            embed_size=embed_size,
            hidden_size=hidden_size,
            vocab_size=vocab_size,
            num_layers=num_layers,
        )

    def forward(self, images: torch.Tensor, captions: torch.Tensor) -> torch.Tensor:
        features = self.encoder(images)
        return self.decoder(features, captions)
