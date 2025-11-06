"""
JSON implementation of ResponseTimeDAO
Reads response time data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import ResponseTimeDAO


class ResponseTimeDAOJSON(ResponseTimeDAO):
    """JSON file implementation of ResponseTimeDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'responseTimes.json'
    
    def get_all(self):
        """Get all response times from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

