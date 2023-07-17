import pyheif
from PIL import Image
import streamlit as st
import os

def heic_to_jpg(heic_path, jpg_path):
    heif_file = pyheif.read(heic_path)
    image = Image.frombytes(
        heif_file.mode, 
        heif_file.size, 
        heif_file.data,
        "raw",
        heif_file.mode,
        heif_file.stride,
    )
    image.save(jpg_path, format="JPEG")
    return jpg_path

# Replace with your file paths
heic_file_path = 'IMG_0695.HEIC'
jpg_file_path = 'file.jpg'

jpg_file_path = heic_to_jpg(heic_file_path, jpg_file_path)

# Create a button for the download
with open(jpg_file_path, 'rb') as f:
    btn = st.download_button(
        label="Download JPG",
        data=f,
        file_name=os.path.basename(jpg_file_path),
        mime='image/jpeg',
    )
