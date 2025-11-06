"""
JSON implementation of PromotionDAO
Reads promotion data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import PromotionDAO


class PromotionDAOJSON(PromotionDAO):
    """JSON file implementation of PromotionDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'promotions.json'
    
    def get_all(self):
        """Get all active promotions from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

