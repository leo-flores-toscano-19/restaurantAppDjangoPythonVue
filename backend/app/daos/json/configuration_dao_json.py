"""
JSON implementation of ConfigurationDAO
Reads configuration data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import ConfigurationDAO


class ConfigurationDAOJSON(ConfigurationDAO):
    """JSON file implementation of ConfigurationDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'configuration.json'
    
    def get_all(self):
        """Get all configuration from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

