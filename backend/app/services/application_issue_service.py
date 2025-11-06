"""
Application Issue Service - Business logic for application issues (chat)
"""
from app.daos.interfaces import ApplicationIssueDAO
from app.daos.json.application_issue_dao_json import ApplicationIssueDAOJSON


class ApplicationIssueService:
    """Service for application issue business logic"""
    
    def __init__(self, dao: ApplicationIssueDAO = None):
        self.dao = dao if dao is not None else ApplicationIssueDAOJSON()
    
    def get_all_application_issues(self):
        """Get all application issues"""
        return self.dao.get_all()
    
    def get_random_application_issue(self):
        """Get random application issue (for chat)"""
        issue = self.dao.get_random()
        if issue:
            return {'response': issue.get('response', 'No response available')}
        return {'response': 'I apologize, but I could not process your request at this time.'}

