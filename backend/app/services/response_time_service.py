"""
Response Time Service - Business logic for response time data
"""
from app.daos.interfaces import ResponseTimeDAO
from app.daos.json.response_time_dao_json import ResponseTimeDAOJSON


class ResponseTimeService:
    """Service for response time business logic"""
    
    def __init__(self, dao: ResponseTimeDAO = None):
        self.dao = dao if dao is not None else ResponseTimeDAOJSON()
    
    def get_all_response_times(self):
        """Get all response times"""
        return self.dao.get_all()
    
    def get_sorted_response_times(self, sort_by: str, sort_direction: str):
        """Get sorted response times"""
        data = self.dao.get_all()
        responses = data.get('responses', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['id', 'responseTime', 'averageTime']
        
        if sort_by in numeric_fields:
            responses.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            responses.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

