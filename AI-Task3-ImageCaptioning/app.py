from pathlib import Path

import streamlit as st
from PIL import Image

from src.captioner import ImageCaptioner
from src.image_utils import load_image


st.set_page_config(
    page_title="Image Captioning",
    page_icon=":camera:",
    layout="centered",
)


@st.cache_resource(show_spinner=False)
def get_captioner() -> ImageCaptioner:
    return ImageCaptioner()


def main() -> None:
    st.title("Image Captioning")
    st.write("Upload an image and generate a short natural-language caption.")

    uploaded_file = st.file_uploader(
        "Choose an image",
        type=["jpg", "jpeg", "png", "webp"],
    )

    sample_path = Path("assets/sample.jpg")
    use_sample = sample_path.exists() and st.button("Use sample image")

    image: Image.Image | None = None

    if uploaded_file is not None:
        image = load_image(uploaded_file)
    elif use_sample:
        image = load_image(sample_path)

    if image is None:
        st.info("Upload an image to get started.")
        return

    st.image(image, caption="Selected image", use_container_width=True)

    with st.spinner("Generating caption..."):
        caption = get_captioner().generate_caption(image)

    st.subheader("Caption")
    st.success(caption)


if __name__ == "__main__":
    main()
