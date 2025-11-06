"""
Delivery Service - Business logic for delivery data
"""
from app.daos.interfaces import DeliveryDAO
from app.daos.json.delivery_dao_json import DeliveryDAOJSON


class DeliveryService:
    """Service for delivery business logic"""
    
    def __init__(self, dao: DeliveryDAO = None):
        self.dao = dao if dao is not None else DeliveryDAOJSON()
    
    def get_all_store_deliveries(self):
        """Get all store deliveries"""
        return self.dao.get_all()
    
    def get_sorted_store_deliveries(self, sort_by: str, sort_direction: str):
        """Get sorted store deliveries"""
        data = self.dao.get_all()
        deliveries = data.get('deliveries', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['orderId', 'deliveryTime', 'distance', 'cost']
        
        if sort_by in numeric_fields:
            deliveries.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            deliveries.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

