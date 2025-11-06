"""
Django REST Framework views for API endpoints
"""
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Import services
from app.services.sales_service import SalesService
from app.services.delivery_service import DeliveryService
from app.services.critical_issues_service import CriticalIssuesService
from app.services.pos_service import PosService
from app.services.promotion_service import PromotionService
from app.services.performance_service import PerformanceService
from app.services.response_time_service import ResponseTimeService
from app.services.weekly_events_service import WeeklyEventsService
from app.services.application_issue_service import ApplicationIssueService
from app.services.ticket_status_service import TicketStatusService
from app.services.feedback_service import FeedbackService
from app.services.configuration_service import ConfigurationService


# Sales endpoints
@api_view(['GET'])
def get_store_sales(request):
    """Get all store sales data"""
    try:
        service = SalesService()
        data = service.get_all_store_sales()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_store_sales_sorted(request):
    """Get sorted store sales data"""
    try:
        sort_by = request.query_params.get('sortBy', 'storeName')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = SalesService()
        data = service.get_sorted_store_sales(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Delivery endpoints
@api_view(['GET'])
def get_store_deliveries(request):
    """Get all store deliveries"""
    try:
        service = DeliveryService()
        data = service.get_all_store_deliveries()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_store_deliveries_sorted(request):
    """Get sorted store deliveries"""
    try:
        sort_by = request.query_params.get('sortBy', 'orderId')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = DeliveryService()
        data = service.get_sorted_store_deliveries(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Critical Issues endpoints
@api_view(['GET'])
def get_critical_issues(request):
    """Get all critical issues"""
    try:
        service = CriticalIssuesService()
        data = service.get_all_critical_issues()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_critical_issues_sorted(request):
    """Get sorted critical issues"""
    try:
        sort_by = request.query_params.get('sortBy', 'id')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = CriticalIssuesService()
        data = service.get_sorted_critical_issues(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# POS Issues endpoints
@api_view(['GET'])
def get_pos_issues(request):
    """Get all POS issues"""
    try:
        service = PosService()
        data = service.get_all_pos_issues()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_pos_issues_sorted(request):
    """Get sorted POS issues"""
    try:
        sort_by = request.query_params.get('sortBy', 'id')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = PosService()
        data = service.get_sorted_pos_issues(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Promotion endpoints
@api_view(['GET'])
def get_promotions(request):
    """Get all active promotions"""
    try:
        service = PromotionService()
        data = service.get_all_promotions()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_promotions_sorted(request):
    """Get sorted promotions"""
    try:
        sort_by = request.query_params.get('sortBy', 'id')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = PromotionService()
        data = service.get_sorted_promotions(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Performance endpoints
@api_view(['GET'])
def get_store_performance(request):
    """Get all store performance data"""
    try:
        service = PerformanceService()
        data = service.get_all_store_performance()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_store_performance_sorted(request):
    """Get sorted store performance"""
    try:
        sort_by = request.query_params.get('sortBy', 'storeName')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = PerformanceService()
        data = service.get_sorted_store_performance(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Response Time endpoints
@api_view(['GET'])
def get_response_times(request):
    """Get all response times"""
    try:
        service = ResponseTimeService()
        data = service.get_all_response_times()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_response_times_sorted(request):
    """Get sorted response times"""
    try:
        sort_by = request.query_params.get('sortBy', 'id')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = ResponseTimeService()
        data = service.get_sorted_response_times(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Weekly Events endpoints
@api_view(['GET'])
def get_weekly_events(request):
    """Get all weekly events"""
    try:
        service = WeeklyEventsService()
        data = service.get_all_weekly_events()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Application Issue endpoints (for chat)
@api_view(['POST'])
def get_application_issue(request):
    """Get random application issue (for chat)"""
    try:
        service = ApplicationIssueService()
        data = service.get_random_application_issue()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_all_application_issues(request):
    """Get all application issues"""
    try:
        service = ApplicationIssueService()
        data = service.get_all_application_issues()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Ticket Status endpoints
@api_view(['POST'])
def get_ticket_status(request):
    """Get ticket status"""
    try:
        service = TicketStatusService()
        data = service.get_ticket_status()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_all_ticket_status(request):
    """Get all ticket statuses"""
    try:
        service = TicketStatusService()
        data = service.get_all_ticket_statuses()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Feedback endpoints
@api_view(['GET'])
def get_positive_feedback(request):
    """Get positive feedback"""
    try:
        service = FeedbackService()
        data = service.get_all_positive_feedback()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_positive_feedback_sorted(request):
    """Get sorted positive feedback"""
    try:
        sort_by = request.query_params.get('sortBy', 'id')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        service = FeedbackService()
        data = service.get_sorted_positive_feedback(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


# Configuration endpoints
@api_view(['POST'])
def get_configuration(request):
    """Get configuration"""
    try:
        service = ConfigurationService()
        data = service.get_configuration()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(['GET'])
def get_all_configuration(request):
    """Get all configuration"""
    try:
        service = ConfigurationService()
        data = service.get_all_configuration()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
