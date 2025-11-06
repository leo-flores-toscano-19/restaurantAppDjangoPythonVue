# Restaurant Manager Dashboard

A modern restaurant manager dashboard application built with Django, Python, and Vue.js.

## 🏗️ Architecture

This application follows a clean architecture pattern with:
- **Django REST Framework** for API endpoints
- **DAO/Repository pattern** for easy data source switching (JSON → PostgreSQL → MongoDB)
- **Service layer** for business logic
- **Model-View-Template (MVT)** pattern for backend
- **Component-based** Vue.js frontend with Tailwind CSS
- **Clean separation** of concerns (models, views, services, serializers, DAOs)
- **Full Python** support throughout

### Data Access Strategy

The application is designed to start with JSON files and easily switch to databases:

1. **Start with JSON files** - All data initially stored in `backend/data/*.json` files
2. **DAO/Repository Pattern** - Abstract data access through DAO interfaces
3. **Easy Database Migration** - Switch to PostgreSQL or MongoDB by changing only a few lines
4. **Service Layer** - Business logic remains unchanged regardless of data source

**Example DAO Pattern:**
```python
# Interface/Abstract Base Class
class SalesDAO(ABC):
    @abstractmethod
    def get_all_store_sales(self):
        pass

# JSON Implementation
class SalesDAOJSON(SalesDAO):
    def get_all_store_sales(self):
        # Read from JSON file
        pass

# PostgreSQL Implementation  
class SalesDAOPostgreSQL(SalesDAO):
    def get_all_store_sales(self):
        # Query from PostgreSQL
        pass

# MongoDB Implementation
class SalesDAOMongoDB(SalesDAO):
    def get_all_store_sales(self):
        # Query from MongoDB
        pass
```

## 📁 Project Structure

```
restaurantAppDjangoPythonVue/
├── backend/                    # Django REST API server
│   ├── manage.py
│   ├── requirements.txt
│   ├── restaurant_app/        # Django project settings
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── app/                    # Main Django app
│   │   ├── models.py          # Django models (for future DB)
│   │   ├── views.py           # API views (Django REST Framework)
│   │   ├── serializers.py     # DRF serializers
│   │   ├── urls.py            # App URL routing
│   │   ├── services/          # Business logic layer
│   │   │   ├── __init__.py
│   │   │   ├── sales_service.py
│   │   │   ├── delivery_service.py
│   │   │   └── ...
│   │   ├── daos/              # Data Access Objects (DAO pattern)
│   │   │   ├── __init__.py
│   │   │   ├── interfaces.py  # Abstract base classes
│   │   │   ├── json/          # JSON implementations
│   │   │   │   ├── __init__.py
│   │   │   │   ├── sales_dao_json.py
│   │   │   │   └── ...
│   │   │   ├── postgresql/    # PostgreSQL implementations
│   │   │   │   ├── __init__.py
│   │   │   │   └── ...
│   │   │   └── mongodb/       # MongoDB implementations
│   │   │       ├── __init__.py
│   │   │       └── ...
│   │   └── tests/             # Django tests
│   │       ├── test_services.py
│   │       ├── test_daos.py
│   │       └── test_views.py
│   └── data/                   # JSON data files
│       ├── salesByStore.json
│       ├── storeDeliveries.json
│       └── ...
├── frontend/                   # Vue.js application
│   ├── package.json
│   ├── vite.config.js
│   ├── tailwind.config.js
│   └── src/
│       ├── main.js
│       ├── App.vue            # Main SPA container
│       ├── components/        # Vue components
│       │   ├── Dashboard.vue
│       │   ├── LeftPanel.vue
│       │   ├── RightPanel.vue
│       │   ├── views/        # View components
│       │   │   ├── SalesView.vue
│       │   │   ├── DeliveriesView.vue
│       │   │   └── ...
│       │   └── ChatView.vue
│       ├── services/          # Frontend API services
│       │   ├── api.js
│       │   └── salesService.js
│       └── assets/
├── IMPLEMENTATION_PLAN.md
├── ARCHITECTURE_EXPLANATION.md
├── TESTING_GUIDE.md
└── README.md
```

## 🚀 Getting Started

### Prerequisites

- Python 3.9+ and pip
- Node.js 18+ and npm (for frontend)
- (Optional) PostgreSQL/MySQL for production database

### Installation

1. **Set up Python Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. **Install Backend Dependencies:**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. **Install Frontend Dependencies:**
   ```bash
   cd frontend
   npm install
   ```
   
   **Note:** The frontend uses Tailwind CSS v3.4.0 with PostCSS. See [FRONTEND.md](./FRONTEND.md) for details on why PostCSS is needed.

4. **Set up Database (if using database):**
   ```bash
   cd backend
   python manage.py migrate
   ```

### Running the Application

1. **Start Backend Server:**
   ```bash
   cd backend
   python manage.py runserver
   ```
   Server runs on http://localhost:8000

2. **Start Frontend (in a new terminal):**
   ```bash
   cd frontend
   npm run dev
   ```
   Frontend runs on http://localhost:5173 (or configured port)

## 📊 Features

### Dashboard Sections (4-Panel Layout)

1. **Left Panel - Reports Section** (Sky/Blue theme)
   - Weekly Events
   - Sales By Store
   - Deliveries
   - POS Issues
   - Performance Metrics
   - Virtual Agent Chat Interface

2. **Middle Panel - Main Content Area**
   - Dynamic view switching
   - Data tables with sorting
   - Chat history display
   - Embedded views for each report

3. **Right Panel - Code Red/Green Section** (Red/Green theme)
   - Critical Issues
   - Positive Feedback
   - Response Time

4. **Right Panel - Promos per Store Section** (Purple/Pink theme)
   - Active Promotions
   - Promo Calendar

### Core Features

- ✅ Sales data visualization with sortable columns
- ✅ Deliveries tracking by store
- ✅ Critical issues management with impact indicators
- ✅ Multi-agent chat interface (Application Issues, Ticket Status, Configuration)
- ✅ Clean, modern UI with Tailwind CSS
- ✅ RESTful API with Django REST Framework
- ✅ DAO pattern for easy data source switching (JSON → PostgreSQL → MongoDB)
- ✅ Unit and integration tests

## 🧪 Testing

### Testing Framework

This project uses **pytest** and **Django's test framework** for testing:
- **Backend**: Django TestCase and pytest for Python unit tests
- **Frontend**: Vitest or Jest for Vue component testing
- **API Testing**: Django REST Framework test client for integration testing

### Quick Start: Running Tests

**1. Install Test Dependencies:**
```bash
# Backend (pytest and coverage should be in requirements.txt)
cd backend
pip install -r requirements.txt

# Frontend
cd frontend
npm install
```

**2. Run All Tests:**
```bash
# Backend tests (Django)
cd backend
python manage.py test

# Or using pytest
pytest

# Frontend tests
cd frontend
npm test
```

**3. Run Tests in Watch Mode (Development):**
```bash
# Backend (pytest watch mode)
cd backend
pytest-watch

# Frontend
cd frontend
npm run test:watch
```

### Test Coverage Validation

**Generate Coverage Reports:**
```bash
# Backend coverage
cd backend
pytest --cov=. --cov-report=html

# Or with coverage.py
coverage run --source='.' manage.py test
coverage report
coverage html

# Frontend coverage
cd frontend
npm test -- --coverage
```

**View Coverage Reports:**
1. Coverage reports are generated in `htmlcov/` directory (backend) or `coverage/` (frontend)
2. Open `htmlcov/index.html` in your browser for interactive report
3. Terminal shows summary table with coverage percentages

**Coverage Metrics:**
- **Statements**: Percentage of code statements executed
- **Branches**: Percentage of conditional branches tested
- **Functions**: Percentage of functions called
- **Lines**: Percentage of lines executed

**Recommended Coverage Targets:**
- Statements: 80%+
- Branches: 75%+
- Functions: 80%+
- Lines: 80%+

### Test Structure

**Backend Tests:**
```
backend/
├── app/
│   ├── tests/
│   │   ├── test_models.py      # Model tests
│   │   ├── test_views.py        # View/API tests
│   │   ├── test_services.py     # Service layer tests
│   │   └── test_serializers.py  # Serializer tests
```

**Frontend Tests:**
```
frontend/
├── tests/
│   ├── components/        # Vue component tests
│   │   ├── dashboard/
│   │   └── views/
│   └── unit/              # Unit tests
```

### Adding New Tests

**Example: Adding a Service Test**
```python
# backend/app/tests/test_services.py
from django.test import TestCase
from app.services import YourService

class YourServiceTestCase(TestCase):
    def setUp(self):
        self.service = YourService()
    
    def test_service_method(self):
        # Arrange
        test_data = {'key': 'value'}
        
        # Act
        result = self.service.method(test_data)
        
        # Assert
        self.assertEqual(result, expected)
```

**Example: Adding a View/API Test**
```python
# backend/app/tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status

class YourViewTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_api_endpoint(self):
        response = self.client.get('/api/endpoint/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
```

**Example: Adding a Component Test**
```javascript
// frontend/tests/components/YourComponent.spec.js
import { mount } from '@vue/test-utils'
import YourComponent from '@/components/YourComponent.vue'

describe('YourComponent', () => {
  it('should render correctly', () => {
    const wrapper = mount(YourComponent)
    expect(wrapper.text()).toContain('Expected')
  })
})
```

### Verifying Tests

**1. Run Tests:**
```bash
# Backend
python manage.py test
# or
pytest

# Frontend
npm test
```

**2. Check Coverage:**
```bash
# Backend
pytest --cov=. --cov-report=html

# Frontend
npm test -- --coverage
```

**3. View HTML Report:**
- Open `htmlcov/index.html` (backend) or `coverage/lcov-report/index.html` (frontend) in browser
- Navigate through files to see:
  - ✅ Green lines = covered by tests
  - ❌ Red lines = not covered
  - 🟡 Yellow lines = partially covered (branches)

**4. Identify Gaps:**
- Look for files with low coverage (< 80%)
- Add tests for uncovered code
- Focus on business logic and error handling first

### Documentation

- **[TESTING_QUICK_START.md](./TESTING_QUICK_START.md)** - Quick start guide for verifying tests
- **[TESTING_GUIDE.md](./TESTING_GUIDE.md)** - Complete testing guide with examples
- **[TESTING.md](./TESTING.md)** - Quick reference for testing patterns

## ⚠️ Deprecation Warnings

During `npm install`, you may see warnings about:
- `inflight@1.0.6` - deprecated package
- `glob@7.2.3` - should use v9+

**These warnings are harmless and come from testing framework dependencies.** They don't affect:
- ✅ Application functionality
- ✅ Test execution
- ✅ Build process

See [DEPRECATION_WARNINGS.md](./DEPRECATION_WARNINGS.md) for detailed explanation and solutions.

## 🔄 Switching Data Sources (JSON → PostgreSQL → MongoDB)

The architecture uses a **DAO/Repository pattern** for easy data source switching. Services remain unchanged!

### Starting with JSON Files

By default, the application uses JSON files in `backend/data/`:

```python
# In services/sales_service.py
from app.daos.json.sales_dao_json import SalesDAOJSON

class SalesService:
    def __init__(self):
        self.dao = SalesDAOJSON()  # JSON implementation
    
    def get_all_store_sales(self):
        return self.dao.get_all_store_sales()
```

### Switching to PostgreSQL

1. **Update Django settings:**
   ```python
   # settings.py
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'restaurant_db',
           'USER': 'your_user',
           'PASSWORD': 'your_password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```

2. **Install PostgreSQL adapter:**
   ```bash
   pip install psycopg2-binary
   ```

3. **Create Django models** (if not already created):
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

4. **Change only the DAO instantiation:**
   ```python
   # In services/sales_service.py - Change only this line!
   from app.daos.postgresql.sales_dao_postgresql import SalesDAOPostgreSQL
   
   class SalesService:
       def __init__(self):
           self.dao = SalesDAOPostgreSQL()  # Changed from SalesDAOJSON
       
       # All other methods remain the same!
   ```

### Switching to MongoDB

1. **Install MongoDB driver:**
   ```bash
   pip install pymongo
   ```

2. **Configure MongoDB connection** (in settings or separate config):
   ```python
   MONGODB_SETTINGS = {
       'host': 'mongodb://localhost:27017/',
       'db': 'restaurant_db'
   }
   ```

3. **Change only the DAO instantiation:**
   ```python
   # In services/sales_service.py - Change only this line!
   from app.daos.mongodb.sales_dao_mongodb import SalesDAOMongoDB
   
   class SalesService:
       def __init__(self):
           self.dao = SalesDAOMongoDB()  # Changed from SalesDAOJSON
       
       # All other methods remain the same!
   ```

**That's it!** Services and business logic remain completely unchanged. Only the DAO implementation changes.

## 📝 Development Status

🚧 **Project in development**

- Phase 1: Project Setup 🚧
- Phase 2: Data Layer (Models & Database) 📋
- Phase 3: Backend Services & API 📋
- Phase 4: Frontend Core 📋
- Phase 5: Frontend Views 📋
- Phase 6: Chat Interface 📋
- Phase 7: Sorting Functionality 📋
- Phase 8: Styling 📋
- Phase 9: Testing Framework 📋

See `BUILD_STATUS.md` for detailed progress (to be created).

## 🛠️ Tech Stack

- **Frontend:** Vue.js 3, Vite, JavaScript/TypeScript, Tailwind CSS
- **Backend:** Django 4+, Django REST Framework, Python 3.9+
- **Data:** JSON files (default), PostgreSQL, MongoDB (easily switchable via DAO pattern)
- **Testing:** pytest, Django TestCase, Vitest/Jest (frontend)
- **Architecture:** DAO/Repository pattern for data access abstraction

### Code Organization & Conventions

This project follows **Django and Python best practices**:

- **Django Conventions:**
  - Apps organized by feature domain
  - Models in `models.py`, Views in `views.py`, URLs in `urls.py`
  - Services in separate `services/` directory
  - DAOs in separate `daos/` directory with implementations by data source

- **Python Conventions:**
  - PEP 8 style guide
  - Type hints where appropriate
  - Abstract base classes for interfaces
  - Independent files for each class/service/DAO
  - Clear separation of concerns

- **File Organization:**
  - One class per file (recommended)
  - Descriptive file names matching class names
  - Clear module structure with `__init__.py` files

- **Frontend Conventions:**
  - Vue.js Composition API with `<script setup>`
  - Component-based architecture
  - Tailwind CSS utility classes (no inline styles)
  - API service layer for all backend communication
  - See [FRONTEND.md](./FRONTEND.md) for detailed frontend documentation

## 📚 Documentation

- **[IMPLEMENTATION_PLAN.md](./IMPLEMENTATION_PLAN.md)** - Detailed implementation guide
- **[ARCHITECTURE_EXPLANATION.md](./ARCHITECTURE_EXPLANATION.md)** - Learning guide for the stack
- **[FRONTEND.md](./FRONTEND.md)** - Frontend documentation (Vue.js, Tailwind CSS, PostCSS explained)
- **[TESTING_QUICK_START.md](./TESTING_QUICK_START.md)** - Quick start: Verify tests & coverage
- **[TESTING_GUIDE.md](./TESTING_GUIDE.md)** - Complete testing guide with examples
- **[TESTING.md](./TESTING.md)** - Quick reference for testing patterns
- **[DEPRECATION_WARNINGS.md](./DEPRECATION_WARNINGS.md)** - Explanation of npm warnings
- **[SETUP.md](./SETUP.md)** - Setup instructions

## 🎯 Next Steps (Optional Enhancements)

1. Add remaining views (POS Issues, Promotions, Performance, etc.)
2. Add more menu options to match original app
3. Enhance chat with more agent types
4. Add filtering/search functionality
5. Add data export features
6. Set up CI/CD pipeline

## 📄 License

ISC

