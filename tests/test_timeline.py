import pytest
import os
import json
from dft.modules.timeline import generate_timeline

def test_generate_timeline(tmp_path):
    events = [
        {'timestamp': '2023-01-02 12:00:00', 'source': 'Browser', 'description': 'Visited Google'},
        {'timestamp': '2023-01-01 10:00:00', 'source': 'System', 'description': 'Boot'},
    ]
    
    json_path = tmp_path / "timeline.json"
    pdf_path = tmp_path / "timeline.pdf"
    
    result = generate_timeline(events, str(json_path), str(pdf_path))
    
    assert result is True
    assert os.path.exists(json_path)
    assert os.path.exists(pdf_path)
    
    # Verify sorting in JSON
    with open(json_path, 'r') as f:
        data = json.load(f)
        assert data[0]['timestamp'] == '2023-01-01 10:00:00' # Should be first
