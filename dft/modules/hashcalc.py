import hashlib
import os
from dft.utils.logger import logger

def calculate_hashes(file_path):
    """
    Calculates MD5, SHA1, and SHA256 hashes for a given file.

    Args:
        file_path (str): Path to the file.

    Returns:
        dict: A dictionary containing 'md5', 'sha1', and 'sha256' hashes,
              or None if the file is not found or an error occurs.
    """
    if not os.path.isfile(file_path):
        logger.error(f"File not found: {file_path}")
        return None

    hashes = {
        'md5': hashlib.md5(),
        'sha1': hashlib.sha1(),
        'sha256': hashlib.sha256()
    }

    try:
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                for algo in hashes.values():
                    algo.update(chunk)
        
        result = {name: algo.hexdigest() for name, algo in hashes.items()}
        logger.info(f"Hashes calculated for {file_path}")
        return result

    except Exception as e:
        logger.error(f"Error calculating hashes for {file_path}: {e}")
        return None
