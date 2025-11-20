import sqlite3
import os
import pandas as pd
from datetime import datetime, timedelta
from dft.utils.logger import logger

def parse_browser_history(db_path):
    """
    Parses a Chrome/Edge history SQLite database.

    Args:
        db_path (str): Path to the 'History' file.

    Returns:
        list: A list of dictionaries containing 'url', 'title', 'visit_count', 'last_visit_time'.
    """
    if not os.path.isfile(db_path):
        logger.error(f"File not found: {db_path}")
        return None

    try:
        # Connect to the database
        # Note: Browser must be closed or file copied to temp location to avoid locks
        conn = sqlite3.connect(f"file:{db_path}?mode=ro", uri=True)
        cursor = conn.cursor()

        # Chrome/Edge store time as microseconds since Jan 1, 1601 UTC
        query = """
        SELECT urls.url, urls.title, urls.visit_count, urls.last_visit_time
        FROM urls
        ORDER BY urls.last_visit_time DESC
        """
        
        cursor.execute(query)
        rows = cursor.fetchall()
        
        history_data = []
        for row in rows:
            url, title, visit_count, last_visit_time = row
            
            # Convert timestamp
            if last_visit_time:
                try:
                    # Windows filetime to datetime
                    dt = datetime(1601, 1, 1) + timedelta(microseconds=last_visit_time)
                    time_str = dt.strftime('%Y-%m-%d %H:%M:%S')
                except:
                    time_str = str(last_visit_time)
            else:
                time_str = "N/A"

            history_data.append({
                'url': url,
                'title': title,
                'visit_count': visit_count,
                'last_visit_time': time_str
            })

        conn.close()
        logger.info(f"Parsed {len(history_data)} history entries from {db_path}")
        return history_data

    except sqlite3.Error as e:
        logger.error(f"SQLite error parsing {db_path}: {e}")
        return None
    except Exception as e:
        logger.error(f"Error parsing history {db_path}: {e}")
        return None

def export_history_csv(history_data, output_path):
    """
    Exports browser history data to CSV.
    """
    if not history_data:
        return False
    
    try:
        df = pd.DataFrame(history_data)
        df.to_csv(output_path, index=False)
        logger.info(f"History data exported to {output_path}")
        return True
    except Exception as e:
        logger.error(f"Error exporting history CSV: {e}")
        return False
