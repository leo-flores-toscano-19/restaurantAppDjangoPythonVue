"""
JSON implementation of PosIssuesDAO
Reads POS issues data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import PosIssuesDAO


class PosIssuesDAOJSON(PosIssuesDAO):
    """JSON file implementation of PosIssuesDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'posIssues.json'
    
    def get_all(self):
        """Get all POS issues from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

