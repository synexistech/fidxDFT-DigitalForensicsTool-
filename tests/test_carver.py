import pytest
import os
from dft.modules.file_carver import carve_files

def test_carve_files(tmp_path):
    # Create a dummy binary file with embedded JPG signature
    bin_path = tmp_path / "dump.bin"
    output_dir = tmp_path / "recovered"
    
    # Fake JPG: FF D8 FF ... FF D9
    fake_jpg = b'\xFF\xD8\xFF\x00\x01\x02\xFF\xD9'
    # Fake PNG: 89 PNG ... IEND ...
    fake_png = b'\x89PNG\r\n\x1a\n\x00\x00\x00\x00IEND\xae\x42\x60\x82'
    
    with open(bin_path, 'wb') as f:
        f.write(b'junkdata')
        f.write(fake_jpg)
        f.write(b'morejunk')
        f.write(fake_png)
        f.write(b'endjunk')
        
    counts = carve_files(str(bin_path), str(output_dir))
    
    assert counts is not None
    assert counts['jpg'] == 1
    assert counts['png'] == 1
    
    assert os.path.exists(output_dir / "recovered_0.jpg")
    assert os.path.exists(output_dir / "recovered_0.png")

def test_carve_files_file_not_found():
    counts = carve_files("non_existent.bin", "output")
    assert counts is None
