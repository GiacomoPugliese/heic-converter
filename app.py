import streamlit as st
import pyheif
from PIL import Image
import os

# Streamlit title
st.title('Local HEIF to JPEG Image Viewer')

# Local HEIF file path
file_path = st.text_input('Enter path to .heic file:', '')

# When user enters a file path
if file_path:
    try:
        # Read HEIF file
        heif_file = pyheif.read(file_path)

        # Convert to PIL Image
        image = Image.frombytes(
            heif_file.mode, 
            heif_file.size, 
            heif_file.data,
            "raw",
            heif_file.mode,
            heif_file.stride,
        )
        
        # Save as JPEG
        jpeg_path = os.path.splitext(file_path)[0] + '.jpg'
        image.save(jpeg_path, 'JPEG')
        
        # Display image
        st.image(jpeg_path)
    except Exception as e:
        st.error(f'Error: {e}')
