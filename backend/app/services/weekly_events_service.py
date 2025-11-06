"""
Weekly Events Service - Business logic for weekly events data
"""
from app.daos.interfaces import WeeklyEventsDAO
from app.daos.json.weekly_events_dao_json import WeeklyEventsDAOJSON


class WeeklyEventsService:
    """Service for weekly events business logic"""
    
    def __init__(self, dao: WeeklyEventsDAO = None):
        self.dao = dao if dao is not None else WeeklyEventsDAOJSON()
    
    def get_all_weekly_events(self):
        """Get all weekly events"""
        return self.dao.get_all()

