import pytest
import os
from dft.modules.hashcalc import calculate_hashes

def test_calculate_hashes(tmp_path):
    # Create a temporary file
    d = tmp_path / "subdir"
    d.mkdir()
    p = d / "hello.txt"
    p.write_text("Hello World")
    
    hashes = calculate_hashes(str(p))
    
    assert hashes is not None
    # Known hashes for "Hello World" (no newline)
    # MD5: b10a8db164e0754105b7a99be72e3fe5
    # SHA1: 0a4d55a8d778e5022fab701977c5d840bbc486d0
    # SHA256: a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e
    
    assert hashes['md5'] == "b10a8db164e0754105b7a99be72e3fe5"
    assert hashes['sha1'] == "0a4d55a8d778e5022fab701977c5d840bbc486d0"
    assert hashes['sha256'] == "a591a6d40bf420404a011733cfb7b190d62c65bf0bcda32b57b277d9ad9f146e"

def test_calculate_hashes_file_not_found():
    hashes = calculate_hashes("non_existent_file.txt")
    assert hashes is None
