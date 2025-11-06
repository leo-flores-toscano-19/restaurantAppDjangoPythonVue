"""
JSON implementation of WeeklyEventsDAO
Reads weekly events data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import WeeklyEventsDAO


class WeeklyEventsDAOJSON(WeeklyEventsDAO):
    """JSON file implementation of WeeklyEventsDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'weeklyEvents.json'
    
    def get_all(self):
        """Get all weekly events from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

