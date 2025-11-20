import os
from dft.utils.logger import logger

def carve_files(binary_path, output_dir):
    """
    Carves JPG and PNG files from a binary file.

    Args:
        binary_path (str): Path to the binary file (e.g., disk image or raw dump).
        output_dir (str): Directory to save recovered files.

    Returns:
        dict: Counts of recovered files {'jpg': count, 'png': count}.
    """
    if not os.path.isfile(binary_path):
        logger.error(f"File not found: {binary_path}")
        return None

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Signatures
    JPG_START = b'\xFF\xD8\xFF'
    JPG_END = b'\xFF\xD9'
    PNG_START = b'\x89PNG\r\n\x1a\n'
    PNG_END = b'IEND\xae\x42\x60\x82'

    recovered_counts = {'jpg': 0, 'png': 0}

    try:
        with open(binary_path, 'rb') as f:
            data = f.read()

        # Carve JPGs
        offset = 0
        while True:
            start = data.find(JPG_START, offset)
            if start == -1:
                break
            
            end = data.find(JPG_END, start)
            if end == -1:
                break
            
            # Include end marker
            end += 2
            
            file_data = data[start:end]
            # Basic validation: max size 10MB
            if len(file_data) < 10 * 1024 * 1024:
                filename = os.path.join(output_dir, f"recovered_{recovered_counts['jpg']}.jpg")
                with open(filename, 'wb') as out:
                    out.write(file_data)
                recovered_counts['jpg'] += 1
            
            offset = end

        # Carve PNGs
        offset = 0
        while True:
            start = data.find(PNG_START, offset)
            if start == -1:
                break
            
            end = data.find(PNG_END, start)
            if end == -1:
                break
            
            # Include end marker
            end += 8
            
            file_data = data[start:end]
            if len(file_data) < 10 * 1024 * 1024:
                filename = os.path.join(output_dir, f"recovered_{recovered_counts['png']}.png")
                with open(filename, 'wb') as out:
                    out.write(file_data)
                recovered_counts['png'] += 1
            
            offset = end

        logger.info(f"Carving complete. Recovered: {recovered_counts}")
        return recovered_counts

    except Exception as e:
        logger.error(f"Error carving files from {binary_path}: {e}")
        return None
