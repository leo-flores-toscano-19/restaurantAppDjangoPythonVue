"""
Sales Service - Business logic for sales data
"""
from app.daos.interfaces import SalesDAO
from app.daos.json.sales_dao_json import SalesDAOJSON


class SalesService:
    """Service for sales business logic"""
    
    def __init__(self, dao: SalesDAO = None):
        # Use JSON DAO by default, but can inject different DAO for testing or future DB migration
        self.dao = dao if dao is not None else SalesDAOJSON()
    
    def get_all_store_sales(self):
        """Get all store sales data"""
        return self.dao.get_all()
    
    def get_sorted_store_sales(self, sort_by: str, sort_direction: str):
        """
        Get sorted store sales data
        
        Args:
            sort_by: Field name to sort by (e.g., 'storeName', 'currentSales')
            sort_direction: 'asc' or 'desc'
        
        Returns:
            Sorted sales data
        """
        data = self.dao.get_all()
        stores = data.get('stores', [])
        
        # Determine if reverse sort
        reverse = sort_direction.lower() == 'desc'
        
        # Numeric fields
        numeric_fields = ['currentSales', 'previousYearSales', 'percentageChange', 'transactions']
        
        if sort_by in numeric_fields:
            # Numeric sorting
            stores.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            # String sorting (case-insensitive)
            stores.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

