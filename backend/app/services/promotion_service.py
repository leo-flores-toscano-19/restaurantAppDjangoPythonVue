"""
Promotion Service - Business logic for promotion data
"""
from app.daos.interfaces import PromotionDAO
from app.daos.json.promotion_dao_json import PromotionDAOJSON


class PromotionService:
    """Service for promotion business logic"""
    
    def __init__(self, dao: PromotionDAO = None):
        self.dao = dao if dao is not None else PromotionDAOJSON()
    
    def get_all_promotions(self):
        """Get all active promotions"""
        return self.dao.get_all()
    
    def get_sorted_promotions(self, sort_by: str, sort_direction: str):
        """Get sorted promotions"""
        data = self.dao.get_all()
        promotions = data.get('promotions', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['id', 'discount', 'startDate', 'endDate']
        
        if sort_by in numeric_fields:
            promotions.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            promotions.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

