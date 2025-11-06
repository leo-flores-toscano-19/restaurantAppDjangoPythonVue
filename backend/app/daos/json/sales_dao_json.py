"""
JSON implementation of SalesDAO
Reads sales data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import SalesDAO


class SalesDAOJSON(SalesDAO):
    """JSON file implementation of SalesDAO"""
    
    def __init__(self):
        # Get path to data directory (3 levels up from this file)
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'salesByStore.json'
    
    def get_all(self):
        """Get all store sales data from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

