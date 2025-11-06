"""
DAO Interfaces (Abstract Base Classes)
These define the contract that all DAO implementations must follow.
"""
from abc import ABC, abstractmethod


class SalesDAO(ABC):
    """Interface for Sales data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all store sales data"""
        pass


class DeliveryDAO(ABC):
    """Interface for Delivery data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all store deliveries"""
        pass


class CriticalIssuesDAO(ABC):
    """Interface for Critical Issues data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all critical issues"""
        pass


class PosIssuesDAO(ABC):
    """Interface for POS Issues data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all POS issues"""
        pass


class PromotionDAO(ABC):
    """Interface for Promotion data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all active promotions"""
        pass


class PerformanceDAO(ABC):
    """Interface for Performance data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all store performance data"""
        pass


class ResponseTimeDAO(ABC):
    """Interface for Response Time data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all response times"""
        pass


class WeeklyEventsDAO(ABC):
    """Interface for Weekly Events data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all weekly events"""
        pass


class ApplicationIssueDAO(ABC):
    """Interface for Application Issue data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all application issues"""
        pass
    
    @abstractmethod
    def get_random(self):
        """Get random application issue"""
        pass


class TicketStatusDAO(ABC):
    """Interface for Ticket Status data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all ticket statuses"""
        pass


class FeedbackDAO(ABC):
    """Interface for Feedback data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all feedback"""
        pass


class ConfigurationDAO(ABC):
    """Interface for Configuration data access"""
    
    @abstractmethod
    def get_all(self):
        """Get all configuration"""
        pass


class CalendarDAO(ABC):
    """Interface for Calendar data access"""
    
    @abstractmethod
    def get_all(self):
        """Get calendar data with events"""
        pass

