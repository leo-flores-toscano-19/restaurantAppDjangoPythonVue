"""
JSON implementation of ApplicationIssueDAO
Reads application issue data from JSON file
"""
import json
import random
from pathlib import Path
from app.daos.interfaces import ApplicationIssueDAO


class ApplicationIssueDAOJSON(ApplicationIssueDAO):
    """JSON file implementation of ApplicationIssueDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'applicationIssues.json'
    
    def get_all(self):
        """Get all application issues from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data
    
    def get_random(self):
        """Get random application issue"""
        data = self.get_all()
        issues = data.get('applicationIssues', [])
        if issues:
            return random.choice(issues)
        return None

