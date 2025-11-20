import pytest
import sqlite3
from dft.modules.browser_history import parse_browser_history

def test_parse_browser_history(tmp_path):
    # Create a dummy SQLite database
    db_path = tmp_path / "History"
    conn = sqlite3.connect(str(db_path))
    cursor = conn.cursor()
    
    # Create table structure similar to Chrome
    cursor.execute("CREATE TABLE urls (id INTEGER PRIMARY KEY, url LONGVARCHAR, title LONGVARCHAR, visit_count INTEGER, typed_count INTEGER, last_visit_time INTEGER, hidden INTEGER)")
    
    # Insert dummy data
    # Time: 13345678900000000 (approx 2023)
    cursor.execute("INSERT INTO urls (url, title, visit_count, last_visit_time) VALUES (?, ?, ?, ?)",
                   ("https://example.com", "Example", 5, 13345678900000000))
    
    conn.commit()
    conn.close()
    
    history = parse_browser_history(str(db_path))
    
    assert history is not None
    assert len(history) == 1
    assert history[0]['url'] == "https://example.com"
    assert history[0]['title'] == "Example"
    assert history[0]['visit_count'] == 5
    # Check if date parsing worked (rough check)
    assert "2023" in history[0]['last_visit_time']

def test_parse_browser_history_file_not_found():
    history = parse_browser_history("non_existent.sqlite")
    assert history is None
