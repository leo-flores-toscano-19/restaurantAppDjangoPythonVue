"""
JSON implementation of FeedbackDAO
Reads feedback data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import FeedbackDAO


class FeedbackDAOJSON(FeedbackDAO):
    """JSON file implementation of FeedbackDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'positiveFeedback.json'
    
    def get_all(self):
        """Get all feedback from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

