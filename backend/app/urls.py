"""
URL routing for app views
"""
from django.urls import path
from app import views

urlpatterns = [
    # Sales endpoints
    path('sales/getStoreSales/', views.get_store_sales, name='get_store_sales'),
    path('sales/getStoreSalesSorted/', views.get_store_sales_sorted, name='get_store_sales_sorted'),
    
    # Delivery endpoints
    path('deliveries/getStoreDeliveries/', views.get_store_deliveries, name='get_store_deliveries'),
    path('deliveries/getStoreDeliveriesSorted/', views.get_store_deliveries_sorted, name='get_store_deliveries_sorted'),
    
    # Critical Issues endpoints
    path('criticalissues/getCriticalIssues/', views.get_critical_issues, name='get_critical_issues'),
    path('criticalissues/getCriticalIssuesSorted/', views.get_critical_issues_sorted, name='get_critical_issues_sorted'),
    
    # POS Issues endpoints
    path('posissues/getPosIssues/', views.get_pos_issues, name='get_pos_issues'),
    path('posissues/getPosIssuesSorted/', views.get_pos_issues_sorted, name='get_pos_issues_sorted'),
    
    # Promotion endpoints
    path('activepromotions/getPromotions/', views.get_promotions, name='get_promotions'),
    path('activepromotions/getPromotionsSorted/', views.get_promotions_sorted, name='get_promotions_sorted'),
    
    # Performance endpoints
    path('performance/getStorePerformance/', views.get_store_performance, name='get_store_performance'),
    path('performance/getStorePerformanceSorted/', views.get_store_performance_sorted, name='get_store_performance_sorted'),
    
    # Response Time endpoints
    path('responsetime/getResponseTimes/', views.get_response_times, name='get_response_times'),
    path('responsetime/getResponseTimesSorted/', views.get_response_times_sorted, name='get_response_times_sorted'),
    
    # Weekly Events endpoints
    path('weeklyevents/getWeeklyEvents/', views.get_weekly_events, name='get_weekly_events'),
    
    # Application Issue endpoints (for chat)
    path('ApplicationIssue/getApplicationIssue/', views.get_application_issue, name='get_application_issue'),
    path('ApplicationIssue/getAllApplicationIssues/', views.get_all_application_issues, name='get_all_application_issues'),
    
    # Ticket Status endpoints
    path('TicketStatus/getTicketStatus/', views.get_ticket_status, name='get_ticket_status'),
    path('TicketStatus/getAllTicketStatus/', views.get_all_ticket_status, name='get_all_ticket_status'),
    
    # Feedback endpoints
    path('positiveFeedback/getPositiveFeedback/', views.get_positive_feedback, name='get_positive_feedback'),
    path('positiveFeedback/getPositiveFeedbackSorted/', views.get_positive_feedback_sorted, name='get_positive_feedback_sorted'),
    
    # Configuration endpoints
    path('Configuration/getConfiguration/', views.get_configuration, name='get_configuration'),
    path('Configuration/getAllConfiguration/', views.get_all_configuration, name='get_all_configuration'),
]

