# Restaurant Manager Dashboard - Implementation Plan

## Project Overview

This document outlines the implementation plan for recreating the Boxlang/ColdBox restaurant manager dashboard application using **Django, Python, Vue.js, and Tailwind CSS** (starting with JSON files, easily switchable to PostgreSQL or MongoDB).

**Note:** For detailed frontend documentation including PostCSS setup, Tailwind CSS configuration, and Vue.js patterns, see [FRONTEND.md](./FRONTEND.md).

---

## Architecture Overview

### Technology Stack Mapping

| Original (Boxlang/ColdBox) | New Stack (Django/Python/Vue.js) |
|---------------------------|----------------------------------|
| **Handlers** (Controllers) | Django Views (DRF) |
| **Services** (Business Logic) | Python Service Classes |
| **Views** (Templates) | Vue.js Components |
| **Layouts** | Vue.js Layout Components |
| **Data Files** (JSON) | JSON files → Future PostgreSQL/MongoDB |
| **Dependency Injection** | Manual DI or dependency injection libraries |
| **CSS Framework** | Tailwind CSS (Build-time) |

### Architecture Pattern: Service-Oriented Architecture (SOA)

While the original app uses HMVC (Hierarchical MVC), the Django/Python/Vue.js stack will use a **Service-Oriented Architecture** that maintains similar separation of concerns:

```
┌─────────────────────────────────────────────────┐
│           Frontend (Vue.js + Tailwind)           │
│  ┌───────────────────────────────────────────┐  │
│  │  Components (UI + State Management)      │  │
│  └───────────────────────────────────────────┘  │
└───────────────────┬─────────────────────────────┘
                    │ HTTP/REST API
┌───────────────────▼─────────────────────────────┐
│         Backend (Django + Python)                │
│  ┌───────────────────────────────────────────┐  │
│  │  Views/Controllers (Request Handling)    │  │
│  │  └─ Services (Business Logic)           │  │
│  │      └─ DAOs (Data Access Layer)         │  │
│  └───────────────────────────────────────────┘  │
└─────────────────────────────────────────────────┘
```

---

## Directory Structure

**Principle: One file = One responsibility. Keep files clean, focused, and small.**

```
restaurantAppDjangoPythonVue/
├── backend/                           # Django REST API server
│   ├── manage.py                      # Django management script
│   ├── requirements.txt               # Python dependencies
│   ├── restaurant_app/                # Django project settings
│   │   ├── settings.py                # Django settings
│   │   ├── urls.py                    # Main URL routing
│   │   └── wsgi.py                    # WSGI config
│   ├── app/                            # Main Django app
│   │   ├── __init__.py
│   │   ├── models.py                  # Django models (for future DB)
│   │   ├── views.py                   # API views (Django REST Framework)
│   │   ├── serializers.py             # DRF serializers
│   │   ├── urls.py                    # App URL routing
│   │   ├── admin.py                   # Django admin config
│   │   ├── services/                  # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── sales_service.py       # Sales business logic
│   │   │   ├── delivery_service.py    # Delivery business logic
│   │   │   ├── critical_issues_service.py
│   │   │   ├── pos_service.py
│   │   │   ├── promotion_service.py
│   │   │   ├── performance_service.py
│   │   │   ├── response_time_service.py
│   │   │   ├── weekly_events_service.py
│   │   │   ├── application_issue_service.py
│   │   │   ├── ticket_status_service.py
│   │   │   ├── feedback_service.py
│   │   │   └── configuration_service.py
│   │   ├── daos/                      # Data Access Objects (DAO pattern)
│   │   │   ├── __init__.py
│   │   │   ├── interfaces.py         # Abstract base classes (interfaces)
│   │   │   ├── json/                  # JSON implementations (current)
│   │   │   │   ├── __init__.py
│   │   │   │   ├── sales_dao_json.py
│   │   │   │   ├── delivery_dao_json.py
│   │   │   │   └── ... (one DAO per feature)
│   │   │   ├── postgresql/            # PostgreSQL implementations (future)
│   │   │   │   ├── __init__.py
│   │   │   │   └── ... (one DAO per feature)
│   │   │   └── mongodb/               # MongoDB implementations (future)
│   │   │       ├── __init__.py
│   │   │       └── ... (one DAO per feature)
│   │   └── tests/                     # Django tests
│   │       ├── __init__.py
│   │       ├── test_services.py
│   │       ├── test_daos.py
│   │       └── test_views.py
│   └── data/                           # JSON data files
│       ├── salesByStore.json
│       ├── storeDeliveries.json
│       ├── criticalIssues.json
│       ├── posIssues.json
│       ├── promotions.json
│       ├── performanceByStore.json
│       ├── responseTimes.json
│       ├── weeklyEvents.json
│       ├── applicationIssues.json
│       ├── ticketStatus.json
│       ├── feedback.json
│       ├── positiveFeedback.json
│       └── configuration.json
│
├── frontend/                           # Vue.js application
│   ├── package.json
│   ├── vite.config.js                 # Vite configuration
│   ├── tailwind.config.js             # Tailwind CSS configuration
│   ├── postcss.config.js              # PostCSS configuration
│   └── src/
│       ├── main.js                    # Vue app entry point
│       ├── App.vue                    # Main SPA container
│       ├── components/                 # Vue components
│       │   ├── Dashboard.vue          # Main dashboard component
│       │   ├── LeftPanel.vue          # Left navigation panel
│       │   ├── RightPanel.vue         # Right panel (Code Red/Green + Promos)
│       │   ├── views/                 # View components
│       │   │   ├── SalesView.vue
│       │   │   ├── DeliveriesView.vue
│       │   │   ├── CriticalIssuesView.vue
│       │   │   ├── PosIssuesView.vue
│       │   │   ├── PromotionsView.vue
│       │   │   ├── PerformanceView.vue
│       │   │   ├── ResponseTimeView.vue
│       │   │   ├── WeeklyEventsView.vue
│       │   │   ├── CalendarView.vue
│       │   │   └── PositiveFeedbackView.vue
│       │   └── ChatView.vue           # Chat interface component
│       ├── services/                   # Frontend API services
│       │   ├── api.js                 # API client setup
│       │   ├── salesService.js        # Sales API calls
│       │   ├── deliveryService.js
│       │   └── ...
│       ├── stores/                    # Pinia stores (if using Pinia)
│       │   └── dashboard.js
│       └── assets/                    # Static assets
│
├── IMPLEMENTATION_PLAN.md
├── ARCHITECTURE_EXPLANATION.md
├── TESTING_GUIDE.md
└── README.md
```

---

## Code Organization Principles

### Clean Code Philosophy

**Core Principle: One file = One responsibility. Keep files small, focused, and readable.**

### File Organization Rules

1. **Separate Concerns**
   - **Components**: Only template and minimal logic
   - **Services**: Business logic only
   - **DAOs**: Data access only
   - **Types**: TypeScript/Python type definitions in dedicated files
   - **Styles**: Tailwind CSS classes (no inline styles)

2. **Component Structure**
   ```vue
   <!-- ✅ GOOD: Clean component -->
   <!-- components/views/SalesView.vue (clean template, ~50 lines) -->
   <template>
     <div class="p-6">
       <h2>Store Sales</h2>
       <SalesTable :stores="stores" />
     </div>
   </template>
   
   <script setup>
   import { ref, onMounted } from 'vue'
   import { fetchSalesData } from '@/services/salesService'
   import SalesTable from './SalesTable.vue'
   
   const stores = ref([])
   
   onMounted(async () => {
     stores.value = await fetchSalesData()
   })
   </script>
   ```

3. **Service Structure**
   ```python
   # ✅ GOOD: Clean service
   # app/services/sales_service.py (business logic only)
   class SalesService:
       def __init__(self):
           self.dao = SalesDAOJSON()
       
       def get_all_store_sales(self):
           return self.dao.get_all()
       
       def get_sorted_store_sales(self, sort_by, sort_direction):
           data = self.dao.get_all()
           # Business logic: sorting
           return sorted_data
   ```

4. **File Naming Conventions**
   - **Python**: `snake_case.py` (e.g., `sales_service.py`)
   - **Vue Components**: `PascalCase.vue` (e.g., `SalesView.vue`)
   - **Services**: `feature_service.py` (e.g., `sales_service.py`)
   - **DAOs**: `feature_dao_source.py` (e.g., `sales_dao_json.py`)

---

## Service and DAO Pattern - Easy Data Source Switching

### Design Goal: 2-3 Line Code Change to Switch from JSON to Database

**Critical Requirement:** The architecture must allow switching from JSON files to PostgreSQL or MongoDB with minimal code changes - ideally just 2-3 lines.

### Understanding Service vs DAO Pattern

**Service Layer (Business Logic):**
- Contains business rules and data transformation
- **NEVER directly accesses files or database**
- Uses DAO interface for all data operations
- Example: `SalesService.get_sorted_store_sales(sort_by, sort_direction)`

**DAO Layer (Data Access Object) - The Abstraction:**
- **Abstracts data source completely**
- Defines interface that Services depend on
- Implementation can be JSON files, PostgreSQL, MongoDB, etc.
- Provides methods like `get_all()`, `get_by_id()`, `save()`, `delete()`
- **This is the key to easy switching!**

### Implementation Strategy: Interface-Based DAO

**Step 1: Define the DAO Interface (Contract)**
```python
# app/daos/interfaces.py - The contract that both implementations follow
from abc import ABC, abstractmethod

class SalesDAO(ABC):
    @abstractmethod
    def get_all(self):
        """Get all store sales data"""
        pass
    
    @abstractmethod
    def get_by_id(self, store_id: str):
        """Get store by ID"""
        pass
```

**Step 2: JSON File Implementation**
```python
# app/daos/json/sales_dao_json.py - JSON file implementation
import json
from pathlib import Path
from app.daos.interfaces import SalesDAO

class SalesDAOJSON(SalesDAO):
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent / 'data' / 'salesByStore.json'
    
    def get_all(self):
        with open(self.data_path, 'r') as f:
            data = json.load(f)
        return data
    
    def get_by_id(self, store_id: str):
        data = self.get_all()
        # Find store by ID
        return next((s for s in data['stores'] if s.get('id') == store_id), None)
```

**Step 3: PostgreSQL Implementation (Future)**
```python
# app/daos/postgresql/sales_dao_postgresql.py - PostgreSQL implementation
from django.db import connection
from app.daos.interfaces import SalesDAO

class SalesDAOPostgreSQL(SalesDAO):
    def get_all(self):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM stores")
            # Convert to dict format
            return {'stores': [...]}
    
    def get_by_id(self, store_id: str):
        with connection.cursor() as cursor:
            cursor.execute("SELECT * FROM stores WHERE id = %s", [store_id])
            # Convert to dict format
            return {...}
```

**Step 4: MongoDB Implementation (Future)**
```python
# app/daos/mongodb/sales_dao_mongodb.py - MongoDB implementation
from pymongo import MongoClient
from app.daos.interfaces import SalesDAO

class SalesDAOMongoDB(SalesDAO):
    def __init__(self, client: MongoClient):
        self.collection = client['restaurant_db']['stores']
    
    def get_all(self):
        stores = list(self.collection.find({}))
        return {'stores': stores}
    
    def get_by_id(self, store_id: str):
        return self.collection.find_one({'_id': store_id})
```

**Step 5: Service Uses DAO Interface (No Direct File/Database Access)**
```python
# app/services/sales_service.py - Uses interface, not implementation
from app.daos.interfaces import SalesDAO

class SalesService:
    # Accept DAO via constructor (Dependency Injection)
    def __init__(self, dao: SalesDAO):
        self.dao = dao
    
    def get_all_store_sales(self):
        # Service doesn't know if it's JSON or PostgreSQL or MongoDB!
        return self.dao.get_all()
    
    def get_sorted_store_sales(self, sort_by: str, sort_direction: str):
        data = self.dao.get_all()
        # Business logic: sorting (same regardless of data source)
        stores = data['stores']
        reverse = sort_direction == 'desc'
        stores.sort(key=lambda x: x[sort_by], reverse=reverse)
        return data
```

**Step 6: Wire Up in Views (THIS IS WHERE YOU SWITCH!)**
```python
# app/views.py - Change implementation here (2-3 lines!)
from app.services.sales_service import SalesService

# ========== JSON FILE VERSION (Current) ==========
from app.daos.json.sales_dao_json import SalesDAOJSON
sales_dao = SalesDAOJSON()
sales_service = SalesService(sales_dao)

# ========== POSTGRESQL VERSION (Future - just swap the 2 lines above) ==========
# from app.daos.postgresql.sales_dao_postgresql import SalesDAOPostgreSQL
# sales_dao = SalesDAOPostgreSQL()
# sales_service = SalesService(sales_dao)

# ========== MONGODB VERSION (Future - just swap the 2 lines above) ==========
# from app.daos.mongodb.sales_dao_mongodb import SalesDAOMongoDB
# from app.utils.mongodb import get_mongo_client
# sales_dao = SalesDAOMongoDB(await get_mongo_client())
# sales_service = SalesService(sales_dao)

@api_view(['GET'])
def get_store_sales(request):
    data = sales_service.get_all_store_sales()
    return Response(data)
```

### The Magic: Switching in 2-3 Lines!

**Current (JSON Files):**
```python
# app/views.py - Lines 5-6
from app.daos.json.sales_dao_json import SalesDAOJSON
sales_dao = SalesDAOJSON()
```

**Future (PostgreSQL):**
```python
# app/views.py - Lines 5-6 (just change these!)
from app.daos.postgresql.sales_dao_postgresql import SalesDAOPostgreSQL
sales_dao = SalesDAOPostgreSQL()
```

**Future (MongoDB):**
```python
# app/views.py - Lines 5-7 (just change these!)
from app.daos.mongodb.sales_dao_mongodb import SalesDAOMongoDB
from app.utils.mongodb import get_mongo_client
sales_dao = SalesDAOMongoDB(get_mongo_client())
```

**That's it!** The Service layer doesn't change at all because it depends on the interface, not the implementation.

---

## Implementation Phases

### Phase 1: Project Setup ✅

**Goal:** Set up Django backend and Vue.js frontend projects

#### Task 1.1: Set up Django Backend
- [ ] Create Python virtual environment
- [ ] Install Django and Django REST Framework
- [ ] Create Django project: `restaurant_app`
- [ ] Create Django app: `app`
- [ ] Configure `settings.py`:
  - [ ] Add `rest_framework` to INSTALLED_APPS
  - [ ] Configure CORS for frontend access
  - [ ] Set up static files
- [ ] Create `requirements.txt` with dependencies
- [ ] Test Django server runs: `python manage.py runserver`

#### Task 1.2: Set up Vue.js Frontend
- [ ] Create Vue.js project with Vite
- [ ] Install dependencies (Vue, Vue Router, Pinia if needed)
- [ ] Configure `vite.config.js` for API proxy
- [ ] Set up Tailwind CSS:
  - [ ] Install Tailwind CSS, PostCSS, Autoprefixer
  - [ ] Create `tailwind.config.js`
  - [ ] Create `postcss.config.js`
  - [ ] Create `src/assets/main.css` with Tailwind directives
- [ ] Test frontend runs: `npm run dev`

#### Task 1.3: Copy JSON Data Files
- [ ] Copy all JSON files from Boxlang project to `backend/data/`
- [ ] Verify JSON files are valid
- [ ] Document data structure for each file

---

### Phase 2: Data Layer (DAO Pattern) ✅

**Goal:** Create DAO interfaces and JSON implementations

#### Task 2.1: Create DAO Interfaces
- [ ] Create `app/daos/interfaces.py`
- [ ] Define abstract base classes for each feature:
  - [ ] `SalesDAO`
  - [ ] `DeliveryDAO`
  - [ ] `CriticalIssuesDAO`
  - [ ] `PosIssuesDAO`
  - [ ] `PromotionDAO`
  - [ ] `PerformanceDAO`
  - [ ] `ResponseTimeDAO`
  - [ ] `WeeklyEventsDAO`
  - [ ] `ApplicationIssueDAO`
  - [ ] `TicketStatusDAO`
  - [ ] `FeedbackDAO`
  - [ ] `ConfigurationDAO`

#### Task 2.2: Create JSON DAO Implementations
- [ ] Create `app/daos/json/` directory
- [ ] Implement JSON DAOs for each feature:
  - [ ] `sales_dao_json.py`
  - [ ] `delivery_dao_json.py`
  - [ ] `critical_issues_dao_json.py`
  - [ ] `pos_issues_dao_json.py`
  - [ ] `promotion_dao_json.py`
  - [ ] `performance_dao_json.py`
  - [ ] `response_time_dao_json.py`
  - [ ] `weekly_events_dao_json.py`
  - [ ] `application_issue_dao_json.py`
  - [ ] `ticket_status_dao_json.py`
  - [ ] `feedback_dao_json.py`
  - [ ] `configuration_dao_json.py`
- [ ] Test each DAO reads JSON files correctly

---

### Phase 3: Service Layer ✅

**Goal:** Create service classes with business logic

#### Task 3.1: Create Service Classes
- [ ] Create `app/services/` directory
- [ ] Implement services for each feature:
  - [ ] `sales_service.py` - `get_all_store_sales()`, `get_sorted_store_sales()`
  - [ ] `delivery_service.py` - `get_all_deliveries()`, `get_sorted_deliveries()`
  - [ ] `critical_issues_service.py` - `get_all_issues()`, `get_sorted_issues()`
  - [ ] `pos_service.py` - `get_all_pos_issues()`, `get_sorted_pos_issues()`
  - [ ] `promotion_service.py` - `get_all_promotions()`, `get_sorted_promotions()`
  - [ ] `performance_service.py` - `get_all_performance()`, `get_sorted_performance()`
  - [ ] `response_time_service.py` - `get_all_response_times()`, `get_sorted_response_times()`
  - [ ] `weekly_events_service.py` - `get_all_events()`
  - [ ] `application_issue_service.py` - `get_random_issue()`, `get_all_issues()`
  - [ ] `ticket_status_service.py` - `get_ticket_status()`, `get_all_ticket_statuses()`
  - [ ] `feedback_service.py` - `get_feedback()`, `get_all_feedback()`
  - [ ] `configuration_service.py` - `get_configuration()`, `get_all_configuration()`
- [ ] Each service should:
  - [ ] Accept DAO in constructor (dependency injection)
  - [ ] Implement business logic (sorting, filtering, calculations)
  - [ ] Return data in consistent format

#### Task 3.2: Implement Sorting Logic
- [ ] Create utility function for sorting (or implement in each service)
- [ ] Handle numeric sorting (sales, percentages, counts)
- [ ] Handle string sorting (store names, dates)
- [ ] Support ascending/descending order

---

### Phase 4: Backend API (Django Views) ✅

**Goal:** Create REST API endpoints

#### Task 4.1: Create API Views
- [ ] Create views in `app/views.py`:
  - [ ] Sales endpoints: `get_store_sales()`, `get_store_sales_sorted()`
  - [ ] Delivery endpoints: `get_store_deliveries()`, `get_store_deliveries_sorted()`
  - [ ] Critical Issues endpoints: `get_critical_issues()`, `get_critical_issues_sorted()`
  - [ ] POS Issues endpoints: `get_pos_issues()`, `get_pos_issues_sorted()`
  - [ ] Promotion endpoints: `get_promotions()`, `get_promotions_sorted()`
  - [ ] Performance endpoints: `get_store_performance()`, `get_store_performance_sorted()`
  - [ ] Response Time endpoints: `get_response_times()`, `get_response_times_sorted()`
  - [ ] Weekly Events endpoints: `get_weekly_events()`
  - [ ] Application Issue endpoints: `get_application_issue()`, `get_all_application_issues()`
  - [ ] Ticket Status endpoints: `get_ticket_status()`, `get_all_ticket_statuses()`
  - [ ] Feedback endpoints: `get_feedback()`, `get_all_feedback()`
  - [ ] Configuration endpoints: `get_configuration()`, `get_all_configuration()`
- [ ] Each view should:
  - [ ] Use `@api_view(['GET'])` decorator
  - [ ] Instantiate service with JSON DAO
  - [ ] Call service method
  - [ ] Return `Response(data)` (auto-converts to JSON)
  - [ ] Handle errors with try/except

#### Task 4.2: Configure URL Routing
- [ ] Create `app/urls.py` with URL patterns
- [ ] Add URL patterns for each endpoint
- [ ] Include app URLs in main `restaurant_app/urls.py`
- [ ] Test all endpoints with Postman/Thunder Client

#### Task 4.3: Configure CORS
- [ ] Install `django-cors-headers`
- [ ] Add to `INSTALLED_APPS`
- [ ] Add CORS middleware
- [ ] Configure CORS settings to allow frontend origin

---

### Phase 5: Frontend Core (Vue.js Setup) ✅

**Goal:** Set up main dashboard structure

#### Task 5.1: Create Main Dashboard Component
- [ ] Create `src/App.vue` - Main SPA container
- [ ] Set up 4-panel layout:
  - [ ] Left Panel (Reports section - Sky/Blue theme)
  - [ ] Middle Panel (Main content area)
  - [ ] Right Panel (Code Red/Green section - Red/Green theme)
  - [ ] Right Panel (Promos per Store section - Purple/Pink theme)
- [ ] Implement view switching logic
- [ ] Add state management (local state or Pinia)

#### Task 5.2: Create Panel Components
- [ ] Create `src/components/LeftPanel.vue`:
  - [ ] Reports section (Sky/Blue gradient)
  - [ ] Virtual Agent chat interface (Blue/Indigo gradient)
  - [ ] Navigation menu items
- [ ] Create `src/components/RightPanel.vue`:
  - [ ] Code Red/Green section (Red/Green gradient)
  - [ ] Promos per Store section (Purple/Pink gradient)
- [ ] Create `src/components/Dashboard.vue` - Main container

#### Task 5.3: Create API Service Layer
- [ ] Create `src/services/api.js` - API client setup
- [ ] Create service files for each feature:
  - [ ] `salesService.js`
  - [ ] `deliveryService.js`
  - [ ] `criticalIssuesService.js`
  - [ ] `posIssuesService.js`
  - [ ] `promotionService.js`
  - [ ] `performanceService.js`
  - [ ] `responseTimeService.js`
  - [ ] `weeklyEventsService.js`
  - [ ] `applicationIssueService.js`
  - [ ] `ticketStatusService.js`
  - [ ] `feedbackService.js`
  - [ ] `configurationService.js`
- [ ] Each service should have methods to fetch data from API

---

### Phase 6: Frontend Views (Vue Components) ✅

**Goal:** Create view components for each feature

#### Task 6.1: Create View Components
- [ ] Create `src/components/views/` directory
- [ ] Create view components:
  - [ ] `SalesView.vue` - Sales by Store table
  - [ ] `DeliveriesView.vue` - Deliveries table
  - [ ] `CriticalIssuesView.vue` - Critical Issues table
  - [ ] `PosIssuesView.vue` - POS Issues table
  - [ ] `PromotionsView.vue` - Active Promotions table
  - [ ] `PerformanceView.vue` - Performance Metrics table
  - [ ] `ResponseTimeView.vue` - Response Time table
  - [ ] `WeeklyEventsView.vue` - Weekly Events list/calendar
  - [ ] `CalendarView.vue` - Promo Calendar
  - [ ] `PositiveFeedbackView.vue` - Positive Feedback table
- [ ] Each view should:
  - [ ] Fetch data on mount
  - [ ] Display data in table format
  - [ ] Show loading state
  - [ ] Show error state
  - [ ] Implement sorting functionality

#### Task 6.2: Implement Table Sorting
- [ ] Add sortable table headers
- [ ] Implement client-side or server-side sorting
- [ ] Show sort direction indicators (arrows)
- [ ] Handle numeric and string sorting

#### Task 6.3: Create Chat View Component
- [ ] Create `src/components/ChatView.vue`
- [ ] Implement chat interface:
  - [ ] Agent selection dropdown
  - [ ] Question input field
  - [ ] Chat history display
  - [ ] Send message functionality
  - [ ] Clear chat functionality
- [ ] Connect to Application Issue, Ticket Status, Configuration endpoints

---

### Phase 7: Styling (Tailwind CSS) ✅

**Goal:** Style all components to match original app

#### Task 7.1: Configure Tailwind Theme
- [ ] Update `tailwind.config.js`:
  - [ ] Add custom colors matching original app
  - [ ] Configure gradients (Sky/Blue, Red/Green, Purple/Pink)
  - [ ] Set up spacing and typography

#### Task 7.2: Style Dashboard Layout
- [ ] Style 4-panel layout:
  - [ ] Left Panel: Sky/Blue gradient theme
  - [ ] Middle Panel: White background
  - [ ] Right Panel: Red/Green and Purple/Pink gradient themes
- [ ] Add responsive design (mobile, tablet, desktop)
- [ ] Add transitions and animations

#### Task 7.3: Style Components
- [ ] Style navigation menu items
- [ ] Style tables (headers, rows, hover states)
- [ ] Style buttons and form inputs
- [ ] Style chat interface
- [ ] Add loading spinners
- [ ] Add error messages

#### Task 7.4: Match Original Design
- [ ] Match color scheme (gray/blue tones)
- [ ] Match typography
- [ ] Match spacing and layout
- [ ] Match button styles
- [ ] Match table styles

---

### Phase 8: Advanced Features ✅

**Goal:** Add advanced functionality

#### Task 8.1: Implement Calendar View
- [ ] Create calendar component
- [ ] Display weekly events
- [ ] Add event details
- [ ] Style calendar to match original

#### Task 8.2: Enhance Chat Interface
- [ ] Add typing indicators
- [ ] Add message timestamps
- [ ] Add agent avatars/icons
- [ ] Improve error handling

#### Task 8.3: Add Filtering/Search
- [ ] Add search functionality to tables
- [ ] Add filter dropdowns
- [ ] Implement client-side filtering

---

### Phase 9: Testing ✅

**Goal:** Write tests for backend and frontend

#### Task 9.1: Backend Tests
- [ ] Set up pytest or Django test framework
- [ ] Write unit tests for services
- [ ] Write unit tests for DAOs
- [ ] Write integration tests for API endpoints
- [ ] Test error handling

#### Task 9.2: Frontend Tests
- [ ] Set up Vitest or Jest
- [ ] Write component tests
- [ ] Write service tests
- [ ] Test user interactions

---

### Phase 10: Documentation & Polish ✅

**Goal:** Finalize documentation and polish

#### Task 10.1: Code Documentation
- [ ] Add docstrings to Python functions/classes
- [ ] Add comments to Vue components
- [ ] Document API endpoints
- [ ] Document data structures

#### Task 10.2: Update README
- [ ] Add setup instructions
- [ ] Add running instructions
- [ ] Add development guidelines
- [ ] Add troubleshooting section

#### Task 10.3: Final Polish
- [ ] Fix any bugs
- [ ] Optimize performance
- [ ] Add error boundaries
- [ ] Improve user experience

---

## Migration Path to PostgreSQL/MongoDB

### When Ready to Switch Data Sources

**Step 1: Create Database DAO Implementations**
- [ ] Create `app/daos/postgresql/` directory
- [ ] Implement PostgreSQL DAOs for each feature
- [ ] OR create `app/daos/mongodb/` directory
- [ ] Implement MongoDB DAOs for each feature

**Step 2: Update Django Settings (for PostgreSQL)**
- [ ] Update `settings.py` DATABASES configuration
- [ ] Install `psycopg2-binary`
- [ ] Run migrations: `python manage.py migrate`

**Step 3: Switch DAO Implementation (2-3 Lines!)**
- [ ] In `app/views.py`, change DAO import and instantiation
- [ ] Test endpoints work correctly
- [ ] Services and business logic remain unchanged!

**Step 4: Seed Database (One-time)**
- [ ] Create script to load JSON data into database
- [ ] Run seed script once
- [ ] Verify data is loaded correctly

---

## Key Design Decisions

### 1. Separation of Concerns
- **Views**: Handle HTTP requests/responses only
- **Services**: All business logic and data processing
- **DAOs**: Data access only (abstracted)
- **Components**: Presentation and user interaction only

### 2. DAO Pattern for Easy Switching
- **Interface-Based**: Services depend on interfaces, not implementations
- **Easy Switching**: Change 2-3 lines to switch data sources
- **No Service Changes**: Business logic stays the same
- **Testable**: Easy to mock DAOs for testing

### 3. Python Conventions
- **PEP 8**: Follow Python style guide
- **Type Hints**: Use type hints where appropriate
- **Docstrings**: Document functions and classes
- **One Class Per File**: Keep files focused

### 4. Vue.js Conventions
- **Composition API**: Use `<script setup>` syntax
- **Component Structure**: Template, script, style sections
- **Reactive Data**: Use `ref()` and `reactive()`
- **Lifecycle Hooks**: Use `onMounted()`, `onUnmounted()`, etc.

### 5. Tailwind CSS Strategy
- **Utility-First**: Use Tailwind utility classes
- **Component Classes**: Create reusable classes in CSS
- **Responsive**: Mobile-first design
- **Match Original**: Match original app's design

---

## Next Steps

1. **Review this implementation plan**
2. **Start with Phase 1: Project Setup**
3. **Follow phases sequentially**
4. **Test each phase before moving to next**
5. **Document any deviations or decisions**

---

## Questions or Clarifications Needed?

- Do you want to use Django's built-in admin interface?
- Preferred state management for Vue? (Local state, Pinia)
- Testing framework preference? (pytest, Django TestCase, Vitest)
- UI component library? (Tailwind CSS only, or add additional libraries?)

**For frontend-specific questions** (PostCSS, Tailwind CSS, Vue.js setup), see [FRONTEND.md](./FRONTEND.md).

Let's discuss and proceed with implementation!

