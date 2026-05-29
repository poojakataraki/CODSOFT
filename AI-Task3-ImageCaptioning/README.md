# Image Captioning

An image captioning project that combines computer vision and natural language processing to generate short captions for uploaded images.

The project includes:

- A ready-to-run Streamlit web app for image caption generation.
- A pretrained transformer captioning pipeline for quick inference.
- A separate ResNet + LSTM training scaffold for experimenting with classic encoder-decoder captioning.
- Clean project structure, reusable modules, and GitHub-friendly documentation.

## Preview

Upload an image in the app and the model returns a natural-language caption.

## Project Structure

```text
AI-Task3-ImageCaptioning/
|-- app.py
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- src/
|   |-- __init__.py
|   |-- captioner.py
|   |-- image_utils.py
|   |-- dataset.py
|   |-- model.py
|   `-- train_resnet_lstm.py
`-- assets/
    `-- .gitkeep
```

## How It Works

Image captioning has two main parts:

1. **Image understanding**: a vision model reads the image and extracts visual features.
2. **Language generation**: a language model uses those features to generate a caption.

For the app, this project uses a pretrained image captioning transformer from Hugging Face. For learning and experimentation, the `src/train_resnet_lstm.py` script shows a traditional ResNet encoder with an LSTM decoder.

## Setup

Create a virtual environment:

```bash
python -m venv .venv
```

Activate it:

```bash
# Windows
.venv\Scripts\activate

# macOS/Linux
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Run the App

```bash
streamlit run app.py
```

Then open the local URL shown in the terminal.

## Using the Captioner in Python

```python
from PIL import Image
from src.captioner import ImageCaptioner

image = Image.open("sample.jpg")
captioner = ImageCaptioner()
caption = captioner.generate_caption(image)

print(caption)
```

You can also run captioning from the command line:

```bash
python -m src.predict path/to/image.jpg
```

## Optional: Train a ResNet + LSTM Model

The training script is included for experimentation. It expects a caption dataset in CSV format:

```csv
image,caption
image_1.jpg,a dog runs through grass
image_1.jpg,a brown dog is playing outside
```

Example:

```bash
python -m src.train_resnet_lstm ^
  --image-dir data/images ^
  --captions data/captions.csv ^
  --epochs 5 ^
  --batch-size 32
```

The script saves checkpoints in `checkpoints/`.

## Notes

- The pretrained app model is downloaded automatically the first time it runs.
- Large folders such as datasets, checkpoints, and model weights are ignored by Git.
- If CUDA is available, inference and training can use the GPU automatically.

## Tech Stack

- Python
- PyTorch
- Transformers
- TorchVision
- Streamlit
- Pillow

## License

This project is open for learning and portfolio use.
