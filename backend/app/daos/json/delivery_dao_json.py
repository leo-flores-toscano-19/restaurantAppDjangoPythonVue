"""
JSON implementation of DeliveryDAO
Reads delivery data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import DeliveryDAO


class DeliveryDAOJSON(DeliveryDAO):
    """JSON file implementation of DeliveryDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'storeDeliveries.json'
    
    def get_all(self):
        """Get all store deliveries from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

