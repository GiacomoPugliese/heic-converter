import pyheif
from PIL import Image

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

# Replace with your file paths
heic_file_path = 'IMG_0695.HEIC'
jpg_file_path = 'file.jpg'

heic_to_jpg(heic_file_path, jpg_file_path)
