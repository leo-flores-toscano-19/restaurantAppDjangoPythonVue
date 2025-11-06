"""
Critical Issues Service - Business logic for critical issues data
"""
from app.daos.interfaces import CriticalIssuesDAO
from app.daos.json.critical_issues_dao_json import CriticalIssuesDAOJSON


class CriticalIssuesService:
    """Service for critical issues business logic"""
    
    def __init__(self, dao: CriticalIssuesDAO = None):
        self.dao = dao if dao is not None else CriticalIssuesDAOJSON()
    
    def get_all_critical_issues(self):
        """Get all critical issues"""
        return self.dao.get_all()
    
    def get_sorted_critical_issues(self, sort_by: str, sort_direction: str):
        """Get sorted critical issues"""
        data = self.dao.get_all()
        issues = data.get('issues', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['id', 'rating', 'affectedUsers']
        
        if sort_by in numeric_fields:
            issues.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            issues.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

