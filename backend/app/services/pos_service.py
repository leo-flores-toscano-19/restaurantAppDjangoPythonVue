"""
POS Issues Service - Business logic for POS issues data
"""
from app.daos.interfaces import PosIssuesDAO
from app.daos.json.pos_issues_dao_json import PosIssuesDAOJSON


class PosService:
    """Service for POS issues business logic"""
    
    def __init__(self, dao: PosIssuesDAO = None):
        self.dao = dao if dao is not None else PosIssuesDAOJSON()
    
    def get_all_pos_issues(self):
        """Get all POS issues"""
        return self.dao.get_all()
    
    def get_sorted_pos_issues(self, sort_by: str, sort_direction: str):
        """Get sorted POS issues"""
        data = self.dao.get_all()
        issues = data.get('issues', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['id', 'rating', 'affectedUsers']
        
        if sort_by in numeric_fields:
            issues.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            issues.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

