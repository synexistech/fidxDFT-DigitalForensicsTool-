import json
import os
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from dft.utils.logger import logger

def generate_timeline(events, output_path_json, output_path_pdf):
    """
    Generates a timeline from a list of events.

    Args:
        events (list): List of dicts {'timestamp': str, 'source': str, 'description': str}.
        output_path_json (str): Path to save JSON timeline.
        output_path_pdf (str): Path to save PDF timeline.
    
    Returns:
        bool: True if successful, False otherwise.
    """
    try:
        # Sort events by timestamp
        sorted_events = sorted(events, key=lambda x: x.get('timestamp', ''))

        # Save JSON
        with open(output_path_json, 'w') as f:
            json.dump(sorted_events, f, indent=4)
        logger.info(f"Timeline JSON saved to {output_path_json}")

        # Save PDF
        c = canvas.Canvas(output_path_pdf, pagesize=letter)
        width, height = letter
        y = height - 50

        c.setFont("Helvetica-Bold", 16)
        c.drawString(50, y, "Digital Forensics Timeline")
        y -= 30
        c.setFont("Helvetica", 10)

        for event in sorted_events:
            if y < 50:
                c.showPage()
                y = height - 50
                c.setFont("Helvetica", 10)
            
            time_str = event.get('timestamp', 'N/A')
            source = event.get('source', 'Unknown')
            desc = event.get('description', 'No description')
            
            # Simple text wrapping or truncation could be added here
            line = f"[{time_str}] ({source}) {desc}"
            c.drawString(50, y, line[:100]) # Truncate to fit page width roughly
            y -= 15

        c.save()
        logger.info(f"Timeline PDF saved to {output_path_pdf}")
        return True

    except Exception as e:
        logger.error(f"Error generating timeline: {e}")
        return False
