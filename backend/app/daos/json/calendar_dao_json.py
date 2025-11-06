"""
JSON implementation of CalendarDAO
Generates calendar data from promotions
"""
import json
from datetime import datetime, date
from calendar import monthrange
from pathlib import Path
from app.daos.interfaces import CalendarDAO


class CalendarDAOJSON(CalendarDAO):
    """JSON file implementation of CalendarDAO"""
    
    def __init__(self):
        self.promotions_path = Path(__file__).parent.parent.parent.parent / 'data' / 'promotions.json'
    
    def get_all(self):
        """Get calendar data with events from promotions"""
        # Load promotions
        with open(self.promotions_path, 'r', encoding='utf-8') as f:
            promotions = json.load(f)
        
        # Get current month and year
        now = datetime.now()
        current_month = now.month
        current_year = now.year
        
        # Get month name
        month_names = [
            'January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'
        ]
        month_name = month_names[current_month - 1]
        
        # Get first day of month and number of days
        first_day_weekday, num_days = monthrange(current_year, current_month)
        
        # Generate calendar days
        days = []
        
        # Add empty cells for days before the first day of the month
        for i in range(first_day_weekday):
            days.append({
                'date': '',
                'day': '',
                'isToday': False
            })
        
        # Add days of the month
        today = date.today()
        for day_num in range(1, num_days + 1):
            day_date = date(current_year, current_month, day_num)
            date_str = day_date.strftime('%Y-%m-%d')
            is_today = day_date == today
            
            days.append({
                'date': date_str,
                'day': str(day_num),
                'isToday': is_today
            })
        
        # Add empty cells to complete the week
        remaining_cells = 7 - (len(days) % 7)
        if remaining_cells < 7:
            for i in range(remaining_cells):
                days.append({
                    'date': '',
                    'day': '',
                    'isToday': False
                })
        
        # Convert promotions to events format
        events = []
        for promo in promotions:
            events.append({
                'title': promo['title'],
                'description': promo['description'],
                'type': promo['type'],
                'date': promo['date']
            })
        
        return {
            'monthName': month_name,
            'year': current_year,
            'days': days,
            'events': events
        }

