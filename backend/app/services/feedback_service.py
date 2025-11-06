"""
Feedback Service - Business logic for feedback data
"""
from app.daos.interfaces import FeedbackDAO
from app.daos.json.feedback_dao_json import FeedbackDAOJSON


class FeedbackService:
    """Service for feedback business logic"""
    
    def __init__(self, dao: FeedbackDAO = None):
        self.dao = dao if dao is not None else FeedbackDAOJSON()
    
    def get_all_positive_feedback(self):
        """Get all positive feedback"""
        return self.dao.get_all()
    
    def get_sorted_positive_feedback(self, sort_by: str, sort_direction: str):
        """Get sorted positive feedback"""
        data = self.dao.get_all()
        feedback = data.get('feedback', [])
        
        reverse = sort_direction.lower() == 'desc'
        numeric_fields = ['id', 'rating', 'date']
        
        if sort_by in numeric_fields:
            feedback.sort(key=lambda x: x.get(sort_by, 0), reverse=reverse)
        else:
            feedback.sort(key=lambda x: str(x.get(sort_by, '')).lower(), reverse=reverse)
        
        return data

