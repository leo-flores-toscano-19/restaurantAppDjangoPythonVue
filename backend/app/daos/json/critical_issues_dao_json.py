"""
JSON implementation of CriticalIssuesDAO
Reads critical issues data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import CriticalIssuesDAO


class CriticalIssuesDAOJSON(CriticalIssuesDAO):
    """JSON file implementation of CriticalIssuesDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'criticalIssues.json'
    
    def get_all(self):
        """Get all critical issues from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

