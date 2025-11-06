"""
JSON implementation of PerformanceDAO
Reads performance data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import PerformanceDAO


class PerformanceDAOJSON(PerformanceDAO):
    """JSON file implementation of PerformanceDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'performanceByStore.json'
    
    def get_all(self):
        """Get all store performance data from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

