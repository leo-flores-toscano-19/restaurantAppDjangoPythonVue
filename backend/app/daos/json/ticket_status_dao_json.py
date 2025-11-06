"""
JSON implementation of TicketStatusDAO
Reads ticket status data from JSON file
"""
import json
from pathlib import Path
from app.daos.interfaces import TicketStatusDAO


class TicketStatusDAOJSON(TicketStatusDAO):
    """JSON file implementation of TicketStatusDAO"""
    
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent.parent / 'data' / 'ticketStatus.json'
    
    def get_all(self):
        """Get all ticket statuses from JSON file"""
        with open(self.data_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        return data

