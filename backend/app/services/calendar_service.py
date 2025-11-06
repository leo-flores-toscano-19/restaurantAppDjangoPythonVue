"""
Calendar Service - Business logic for calendar data
"""
from app.daos.interfaces import CalendarDAO
from app.daos.json.calendar_dao_json import CalendarDAOJSON


class CalendarService:
    """Service for calendar business logic"""
    
    def __init__(self, dao: CalendarDAO = None):
        self.dao = dao if dao is not None else CalendarDAOJSON()
    
    def get_calendar_data(self):
        """Get calendar data with events"""
        return self.dao.get_all()

