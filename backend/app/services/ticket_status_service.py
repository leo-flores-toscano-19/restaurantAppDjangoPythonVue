"""
Ticket Status Service - Business logic for ticket status data
"""
from app.daos.interfaces import TicketStatusDAO
from app.daos.json.ticket_status_dao_json import TicketStatusDAOJSON


class TicketStatusService:
    """Service for ticket status business logic"""
    
    def __init__(self, dao: TicketStatusDAO = None):
        self.dao = dao if dao is not None else TicketStatusDAOJSON()
    
    def get_all_ticket_statuses(self):
        """Get all ticket statuses"""
        return self.dao.get_all()
    
    def get_ticket_status(self):
        """Get ticket status (returns random or first)"""
        data = self.dao.get_all()
        statuses = data.get('ticketStatuses', [])
        if statuses:
            return statuses[0]  # Return first status, can be modified to return random
        return {'status': 'No status available'}

