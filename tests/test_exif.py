import pytest
from dft.modules.exif_extractor import extract_exif
from PIL import Image
import os

def test_extract_exif_no_data(tmp_path):
    # Create a dummy image without EXIF
    img_path = tmp_path / "test_image.jpg"
    image = Image.new('RGB', (100, 100), color = 'red')
    image.save(img_path)
    
    exif_data = extract_exif(str(img_path))
    # Should return empty dict or None depending on implementation for no EXIF
    # Our implementation returns {} if no EXIF found but file exists
    assert exif_data == {} or exif_data is None

def test_extract_exif_file_not_found():
    exif_data = extract_exif("non_existent_image.jpg")
    assert exif_data is None
