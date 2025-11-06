"""
Performance Service - Business logic for performance data
"""
from app.daos.interfaces import PerformanceDAO
from app.daos.json.performance_dao_json import PerformanceDAOJSON


class PerformanceService:
    """Service for performance business logic"""
    
    def __init__(self, dao: PerformanceDAO = None):
        self.dao = dao if dao is not None else PerformanceDAOJSON()
    
    def get_all_store_performance(self):
        """Get all store performance data"""
        return self.dao.get_all()
    
    def get_sorted_store_performance(self, sort_by: str, sort_direction: str):
        """Get sorted store performance"""
        data = self.dao.get_all()
        stores = data.get('stores', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['averageResponseTime', 'uptime', 'errorRate']
        
        if sort_by in numeric_fields:
            stores.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            stores.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

