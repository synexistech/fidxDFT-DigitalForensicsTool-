from PIL import Image
from PIL.ExifTags import TAGS
import os
from dft.utils.logger import logger

def extract_exif(image_path):
    """
    Extracts EXIF metadata from an image file.

    Args:
        image_path (str): Path to the image file.

    Returns:
        dict: A dictionary of EXIF tags and values, or None if no EXIF data found or error.
    """
    if not os.path.isfile(image_path):
        logger.error(f"File not found: {image_path}")
        return None

    try:
        image = Image.open(image_path)
        exif_data = image._getexif()

        if not exif_data:
            logger.info(f"No EXIF data found in {image_path}")
            return {}

        exif_dict = {}
        for tag_id, value in exif_data.items():
            tag_name = TAGS.get(tag_id, tag_id)
            # Decode bytes to string if possible for readability
            if isinstance(value, bytes):
                try:
                    value = value.decode()
                except:
                    pass
            exif_dict[tag_name] = value
            
        logger.info(f"EXIF data extracted from {image_path}")
        return exif_dict

    except Exception as e:
        logger.error(f"Error extracting EXIF from {image_path}: {e}")
        return None
