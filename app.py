import streamlit as st
import pyheif
from PIL import Image
import io
import requests

def convert_heif_to_jpg(image_id):
    # Get the file content from Google Drive
    url = f"https://drive.google.com/uc?id={image_id}"
    response = requests.get(url)

    # Convert the HEIF image to JPG
    heif_image = pyheif.read_heif(response.content)
    jpg_image = Image.frombytes(
        heif_image.mode,
        heif_image.size,
        heif_image.data,
        "raw",
        heif_image.mode,
        heif_image.stride,
    )

    return jpg_image

def main():
    st.title("HEIF to JPG Converter")

    # Input image ID from the user
    image_id = st.text_input("Enter Google Drive Image ID")

    if st.button("Convert"):
        if image_id:
            try:
                # Convert HEIF to JPG
                jpg_image = convert_heif_to_jpg(image_id)

                # Display the converted image
                st.image(jpg_image, caption="Converted Image", use_column_width=True)
            except Exception as e:
                st.error(f"Error: {str(e)}")
        else:
            st.warning("Please enter a valid Google Drive Image ID")

if __name__ == "__main__":
    main()

