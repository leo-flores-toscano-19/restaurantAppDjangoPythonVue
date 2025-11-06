# Architecture Explanation - Restaurant Manager Dashboard

## Learning Guide for Django/Python/Vue.js Stack

This document explains the architecture and code patterns used in this application, designed for developers migrating from Boxlang/ColdBox to Django/Python/Vue.js.

---

## Table of Contents

1. [Overview of the Stack](#overview-of-the-stack)
2. [Architecture Layers Explained](#architecture-layers-explained)
3. [How It Maps from Boxlang/ColdBox](#how-it-maps-from-boxlangcoldbox)
4. [Service and DAO Pattern Explained](#service-and-dao-pattern-explained)
5. [Frontend Patterns (Vue.js)](#frontend-patterns-vuejs)
6. [Backend Patterns (Django + Python)](#backend-patterns-django--python)
7. [Data Flow Examples](#data-flow-examples)
8. [Key Concepts Explained](#key-concepts-explained)

**Note:** For detailed frontend documentation including PostCSS, Tailwind CSS setup, and Vue.js patterns, see [FRONTEND.md](./FRONTEND.md).

---

## Overview of the Stack

### What is Django?

**Django** is a high-level Python web framework that provides:
- **Model-View-Template (MVT)** architecture (similar to MVC)
- **Object-Relational Mapping (ORM)** for database operations
- **Admin interface** for managing data
- **URL routing** and request handling
- **Built-in security** features
- **RESTful API** support via Django REST Framework

**Why use Django instead of plain Python?**
- Batteries included - many features built-in
- Follows "Don't Repeat Yourself" (DRY) principle
- Large ecosystem and community
- Excellent documentation
- Production-ready out of the box

**Think of it as:** The "ColdBox" framework equivalent for Python

### What is Django REST Framework (DRF)?

**Django REST Framework** is a toolkit for building REST APIs with Django:
- **Serializers** - Convert Python objects to JSON (like ColdBox's `renderData()`)
- **ViewSets** - Handle API endpoints (like ColdBox Handlers)
- **Routers** - Automatic URL routing for APIs
- **Authentication** - Built-in auth support
- **Permissions** - Fine-grained access control

**Why use DRF?**
- Makes building REST APIs easy
- Handles JSON serialization automatically
- Provides browsable API interface
- Consistent API structure

### What is Vue.js?

**Vue.js** is a progressive JavaScript framework for building user interfaces:
- **Reactive data binding** - UI updates automatically when data changes
- **Component-based** - Build reusable UI components
- **Template syntax** - Write HTML-like templates
- **Single Page Application (SPA)** support
- **Lightweight** - Smaller than React or Angular

**Why use Vue.js?**
- Easy to learn (especially coming from Alpine.js)
- Great documentation
- Flexible - can be used incrementally
- Similar syntax to Alpine.js (which you used in Boxlang project)

**Think of it as:** A more powerful version of Alpine.js

### What is Python?

**Python** is a high-level programming language that:
- Is easy to read and write
- Has a huge standard library
- Supports multiple programming paradigms
- Is widely used for web development, data science, automation

**Key Python Concepts:**
- **Indentation matters** - Python uses indentation instead of braces `{}`
- **Dynamic typing** - Variables don't need type declarations (but we can use type hints)
- **Everything is an object** - Functions, classes, modules are all objects
- **Package management** - Use `pip` to install packages (like npm for Node.js)

---

## Architecture Layers Explained

### Three-Layer Architecture

```
┌─────────────────────────────────────┐
│   Presentation Layer (Frontend)     │
│   Vue.js Components                 │
│   - User Interface                   │
│   - User Interactions                │
│   - State Management                 │
└──────────────┬──────────────────────┘
               │ HTTP Requests
               │ (REST API)
┌──────────────▼──────────────────────┐
│   Application Layer (Backend)        │
│   Django Views + Services            │
│   - Request Handling                 │
│   - Business Logic                   │
│   - Data Processing                  │
└──────────────┬──────────────────────┘
               │ Data Access
               │
┌──────────────▼──────────────────────┐
│   Data Layer                         │
│   JSON Files → PostgreSQL → MongoDB  │
│   - Data Storage                     │
│   - Data Retrieval                   │
└──────────────────────────────────────┘
```

### Layer Responsibilities

#### 1. Presentation Layer (Frontend - Vue.js)
**What it does:**
- Displays data to users
- Handles user clicks, form submissions
- Manages UI state (what's visible, what's loading)
- Makes HTTP requests to backend

**Example:**
```vue
<!-- components/views/SalesView.vue -->
<template>
  <div>
    <table>
      <tr v-for="store in stores" :key="store.storeName">
        <td>{{ store.storeName }}</td>
        <td>${{ store.currentSales }}</td>
      </tr>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const stores = ref([])

onMounted(async () => {
  const response = await fetch('/api/sales/getStoreSales/')
  const data = await response.json()
  stores.value = data.stores
})
</script>
```

#### 2. Application Layer (Backend - Django)
**What it does:**
- Receives HTTP requests
- Processes business logic (sorting, filtering, calculations)
- Coordinates data access
- Returns JSON responses

**Example:**
```python
# app/views.py - Django View (like a Handler in ColdBox)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.services.sales_service import SalesService

@api_view(['GET'])
def get_store_sales(request):
    # Call service to get data
    sales_service = SalesService()
    data = sales_service.get_all_store_sales()
    
    # Return JSON response
    return Response(data)

# app/services/sales_service.py - Service (like a Service in ColdBox)
class SalesService:
    def __init__(self):
        self.dao = SalesDAOJSON()  # DAO for data access
    
    def get_all_store_sales(self):
        # Access data layer
        data = self.dao.get_all()
        return data
```

#### 3. Data Layer (DAO Pattern)
**What it does:**
- Reads/writes data from storage
- Abstracts data source (JSON file, PostgreSQL, MongoDB)
- Provides consistent interface regardless of data source

**Example:**
```python
# app/daos/json/sales_dao_json.py - JSON Implementation
import json
from pathlib import Path

class SalesDAOJSON:
    def __init__(self):
        self.data_path = Path(__file__).parent.parent.parent / 'data' / 'salesByStore.json'
    
    def get_all(self):
        # Read JSON file
        with open(self.data_path, 'r') as f:
            data = json.load(f)
        return data
```

---

## How It Maps from Boxlang/ColdBox

### Handler → Django View

**Boxlang/ColdBox:**
```cfml
// handlers/Sales.cfc
component {
    property name="salesService" inject="models.SalesService";
    
    function getStoreSales(event, rc, prc) {
        var salesData = salesService.getAllStoreSales();
        event.renderData(type="json", data=salesData);
    }
}
```

**Django/Python:**
```python
# app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.services.sales_service import SalesService

@api_view(['GET'])
def get_store_sales(request):
    sales_service = SalesService()
    sales_data = sales_service.get_all_store_sales()
    return Response(sales_data)  # Automatically converts to JSON
```

**Key Differences:**
- ColdBox uses dependency injection (`inject="models.SalesService"`)
- Django uses manual instantiation (or dependency injection libraries)
- ColdBox uses `event.renderData()`, Django uses `Response()` which auto-converts to JSON
- Django uses decorators (`@api_view`) to define HTTP methods

### Service → Service (Same Concept!)

**Boxlang/ColdBox:**
```cfml
// models/SalesService.cfc
component {
    function getAllStoreSales() {
        var jsonFile = expandPath("/data/salesByStore.json");
        var jsonContent = fileRead(jsonFile);
        return deserializeJSON(jsonContent);
    }
}
```

**Django/Python:**
```python
# app/services/sales_service.py
import json
from pathlib import Path
from app.daos.json.sales_dao_json import SalesDAOJSON

class SalesService:
    def __init__(self):
        self.dao = SalesDAOJSON()  # Use DAO for data access
    
    def get_all_store_sales(self):
        return self.dao.get_all()  # DAO handles file reading
```

**Key Differences:**
- ColdBox uses `expandPath()` and `fileRead()`
- Python uses `Path` and `open()` for file operations
- Python uses `json.load()` instead of `deserializeJSON()`
- Same business logic, different syntax!

### View → Vue Component

**Boxlang/ColdBox:**
```cfml
<!-- views/sales/index.cfm -->
<cfoutput>
  <table>
    <cfloop array="#stores#" index="store">
      <tr>
        <td>#store.storeName#</td>
        <td>#store.currentSales#</td>
      </tr>
    </cfloop>
  </table>
</cfoutput>
```

**Vue.js:**
```vue
<!-- components/views/SalesView.vue -->
<template>
  <table>
    <tr v-for="store in stores" :key="store.storeName">
      <td>{{ store.storeName }}</td>
      <td>{{ store.currentSales }}</td>
    </tr>
  </table>
</template>

<script setup>
import { ref } from 'vue'

const stores = ref([])
</script>
```

**Key Differences:**
- ColdBox uses server-side rendering with CFML tags (`<cfloop>`)
- Vue uses client-side rendering with directives (`v-for`)
- Vue needs `ref()` for reactive data
- Vue uses `v-for` instead of `<cfloop>`
- Vue uses `{{ }}` for interpolation (similar to `# #` in CFML)

---

## Service and DAO Pattern Explained

### Why Separate Service and DAO?

**Service Layer (Business Logic):**
- Contains business rules
- Handles data transformation
- Coordinates multiple data sources
- Example: Sorting, filtering, calculations

**DAO Layer (Data Access Object):**
- Handles data storage/retrieval
- Abstracts data source (JSON file, PostgreSQL, MongoDB)
- Easy to swap data sources later

### Example: Service + DAO Pattern

```python
# ========== DAO Layer (Data Access) ==========
# app/daos/interfaces.py - Abstract Base Class (Interface)
from abc import ABC, abstractmethod

class SalesDAO(ABC):
    @abstractmethod
    def get_all(self):
        """Get all store sales data"""
        pass

# app/daos/json/sales_dao_json.py - JSON Implementation
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

# ========== Service Layer (Business Logic) ==========
# app/services/sales_service.py
from app.daos.json.sales_dao_json import SalesDAOJSON

class SalesService:
    def __init__(self):
        self.dao = SalesDAOJSON()  # Use JSON DAO
    
    # Simple data retrieval
    def get_all_store_sales(self):
        return self.dao.get_all()
    
    # Business logic: Sorting
    def get_sorted_store_sales(self, sort_by: str, sort_direction: str):
        data = self.dao.get_all()
        stores = data['stores']
        
        # Business logic: Sort the data
        reverse = sort_direction == 'desc'
        
        if sort_by in ['currentSales', 'previousYearSales', 'percentageChange', 'transactions']:
            # Numeric sorting
            stores.sort(key=lambda x: x[sort_by], reverse=reverse)
        else:
            # String sorting
            stores.sort(key=lambda x: x[sort_by].lower(), reverse=reverse)
        
        return data
```

### The Magic: Switching Data Sources in 2-3 Lines!

**Current (JSON Files):**
```python
# app/services/sales_service.py
from app.daos.json.sales_dao_json import SalesDAOJSON

class SalesService:
    def __init__(self):
        self.dao = SalesDAOJSON()  # JSON implementation
```

**Future (PostgreSQL):**
```python
# app/services/sales_service.py - Change only this line!
from app.daos.postgresql.sales_dao_postgresql import SalesDAOPostgreSQL

class SalesService:
    def __init__(self):
        self.dao = SalesDAOPostgreSQL()  # Changed from SalesDAOJSON
```

**Future (MongoDB):**
```python
# app/services/sales_service.py - Change only this line!
from app.daos.mongodb.sales_dao_mongodb import SalesDAOMongoDB

class SalesService:
    def __init__(self):
        self.dao = SalesDAOMongoDB()  # Changed from SalesDAOJSON
```

**That's it!** All business logic in `SalesService` remains unchanged because it depends on the interface, not the implementation.

---

## Frontend Patterns (Vue.js)

### Component Structure

```vue
<!-- components/views/SalesView.vue -->
<template>
  <div class="p-6">
    <h2 class="text-2xl font-bold mb-4">Store Sales</h2>
    
    <div v-if="loading" class="text-center">
      Loading...
    </div>
    
    <div v-else-if="error" class="text-red-500">
      Error: {{ error }}
    </div>
    
    <table v-else class="min-w-full">
      <thead>
        <tr>
          <th>Store Name</th>
          <th>Current Sales</th>
          <th>Previous Year</th>
          <th>Change %</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="store in stores" :key="store.storeName">
          <td>{{ store.storeName }}</td>
          <td>${{ formatCurrency(store.currentSales) }}</td>
          <td>${{ formatCurrency(store.previousYearSales) }}</td>
          <td>{{ store.percentageChange }}%</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const stores = ref([])
const loading = ref(false)
const error = ref(null)

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0
  }).format(value)
}

onMounted(async () => {
  loading.value = true
  error.value = null
  
  try:
    const response = await fetch('/api/sales/getStoreSales/')
    if (!response.ok) throw new Error('Failed to fetch')
    const data = await response.json()
    stores.value = data.stores
  except (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
})
</script>
```

### Key Vue.js Concepts

#### 1. Reactive Data with `ref()`
```javascript
const stores = ref([])  // Creates reactive reference
stores.value = [...]    // Access/modify with .value
```

#### 2. Template Directives
```vue
<!-- v-if: Conditional rendering -->
<div v-if="loading">Loading...</div>

<!-- v-for: Loop through array -->
<tr v-for="store in stores" :key="store.storeName">

<!-- v-model: Two-way data binding -->
<input v-model="searchQuery">

<!-- :key: Bind attributes -->
<div :class="{ active: isActive }">
```

#### 3. Lifecycle Hooks
```javascript
import { onMounted, onUnmounted } from 'vue'

onMounted(() => {
  // Runs when component is mounted (like componentDidMount in React)
  loadData()
})

onUnmounted(() => {
  // Runs when component is unmounted (cleanup)
  cleanup()
})
```

#### 4. Computed Properties
```javascript
import { computed } from 'vue'

const sortedStores = computed(() => {
  return stores.value.sort((a, b) => {
    return a.storeName.localeCompare(b.storeName)
  })
})
```

### State Management

**Option 1: Local State (Component-level)**
```vue
<script setup>
const stores = ref([])  // State only in this component
</script>
```

**Option 2: Pinia (Global State Management)**
```javascript
// stores/dashboard.js
import { defineStore } from 'pinia'

export const useDashboardStore = defineStore('dashboard', {
  state: () => ({
    currentView: 'weeklyevents',
    stores: [],
    loading: false
  }),
  
  actions: {
    setView(view) {
      this.currentView = view
    },
    
    async loadSalesData() {
      this.loading = true
      // Fetch data...
      this.loading = false
    }
  }
})
```

**Recommendation:** Start with **local state** for simplicity. If state becomes complex, migrate to Pinia.

---

## Backend Patterns (Django + Python)

### Django View Structure

```python
# app/views.py
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from app.services.sales_service import SalesService

@api_view(['GET'])
def get_store_sales(request):
    try:
        sales_service = SalesService()
        data = sales_service.get_all_store_sales()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(['GET'])
def get_store_sales_sorted(request):
    try:
        sort_by = request.query_params.get('sortBy', 'storeName')
        sort_direction = request.query_params.get('sortDirection', 'asc')
        
        sales_service = SalesService()
        data = sales_service.get_sorted_store_sales(sort_by, sort_direction)
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
```

### URL Routing

```python
# app/urls.py
from django.urls import path
from app import views

urlpatterns = [
    path('sales/getStoreSales/', views.get_store_sales, name='get_store_sales'),
    path('sales/getStoreSalesSorted/', views.get_store_sales_sorted, name='get_store_sales_sorted'),
    # ... other routes
]

# restaurant_app/urls.py (main project URLs)
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('app.urls')),  # Include app URLs
]
```

### Key Django Concepts

#### 1. Decorators
```python
@api_view(['GET'])  # Decorator - modifies function behavior
def my_view(request):
    pass
```

#### 2. Request Object
- `request.method`: HTTP method (GET, POST, etc.)
- `request.query_params`: URL query parameters (`?sortBy=name`)
- `request.data`: Request body (for POST/PUT)

#### 3. Response Object
```python
return Response(data)  # Automatically converts to JSON
return Response(data, status=status.HTTP_200_OK)
```

#### 4. Query Parameters
```python
sort_by = request.query_params.get('sortBy', 'storeName')  # Get with default
sort_direction = request.query_params.get('sortDirection', 'asc')
```

---

## Data Flow Examples

### Example 1: Loading Sales Data

```
User clicks "Sales" button
    ↓
Frontend: SalesView component
    ↓
onMounted hook triggers
    ↓
fetch('/api/sales/getStoreSales/')
    ↓
HTTP GET request to backend
    ↓
Backend: Django URL routing
    ↓
app/urls.py → views.get_store_sales
    ↓
Calls SalesService.get_all_store_sales()
    ↓
Service calls SalesDAO.get_all()
    ↓
DAO reads JSON file from filesystem
    ↓
Returns data back up the chain
    ↓
Service returns data to view
    ↓
View sends JSON response
    ↓
Frontend receives JSON
    ↓
stores.value = data.stores (updates reactive state)
    ↓
Vue re-renders component with new data
    ↓
User sees sales table
```

### Example 2: Sorting Sales Data

```
User clicks table header "Store Name"
    ↓
Frontend: handleSort('storeName')
    ↓
Updates sortBy state
    ↓
fetch(`/api/sales/getStoreSalesSorted/?sortBy=storeName&sortDirection=asc`)
    ↓
Backend: Django URL routing
    ↓
Extracts query params: request.query_params.get('sortBy')
    ↓
Calls SalesService.get_sorted_store_sales('storeName', 'asc')
    ↓
Service gets all data from DAO
    ↓
Service applies sorting logic (business logic)
    ↓
Returns sorted data
    ↓
Frontend receives sorted JSON
    ↓
Updates stores state
    ↓
Table re-renders with sorted data
```

---

## Key Concepts Explained

### 1. Python Syntax Basics

**Indentation:**
```python
# Python uses indentation instead of braces
if condition:
    do_something()  # Indented = inside if block
    do_another()    # Still inside if block
do_outside()       # Not indented = outside if block
```

**Variables:**
```python
# No type declaration needed (but can use type hints)
store_name = "Downtown"  # String
current_sales = 1250000  # Integer
percentage = 5.93        # Float
is_active = True         # Boolean
```

**Functions:**
```python
def get_all_store_sales():
    return data

# With type hints (optional but recommended)
def get_all_store_sales() -> dict:
    return data
```

**Classes:**
```python
class SalesService:
    def __init__(self):  # Constructor
        self.dao = SalesDAOJSON()
    
    def get_all_store_sales(self):  # Method
        return self.dao.get_all()
```

### 2. Python File Operations

**Reading JSON:**
```python
import json
from pathlib import Path

# Using pathlib (modern way)
data_path = Path(__file__).parent / 'data' / 'salesByStore.json'
with open(data_path, 'r') as f:
    data = json.load(f)

# Using string path (older way)
with open('/path/to/file.json', 'r') as f:
    data = json.load(f)
```

### 3. Django REST Framework

**Serializers (Convert Python objects to JSON):**
```python
# app/serializers.py
from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    storeName = serializers.CharField()
    currentSales = serializers.IntegerField()
    previousYearSales = serializers.IntegerField()
```

**ViewSets (Alternative to function-based views):**
```python
# app/views.py
from rest_framework import viewsets
from rest_framework.response import Response

class SalesViewSet(viewsets.ViewSet):
    def list(self, request):
        # GET /api/sales/
        service = SalesService()
        data = service.get_all_store_sales()
        return Response(data)
```

### 4. Vue.js Composition API

**Setup Script (Modern Vue 3 syntax):**
```vue
<script setup>
// Variables are automatically exposed to template
const stores = ref([])
const loading = ref(false)

// Functions are automatically exposed
const loadData = async () => {
  // ...
}
</script>
```

**Options API (Alternative syntax):**
```vue
<script>
export default {
  data() {
    return {
      stores: [],
      loading: false
    }
  },
  
  methods: {
    async loadData() {
      // ...
    }
  }
}
</script>
```

---

## Common Patterns Summary

### Pattern 1: Fetch Data on Component Mount
```vue
<script setup>
import { ref, onMounted } from 'vue'

const stores = ref([])

onMounted(async () => {
  const response = await fetch('/api/sales/getStoreSales/')
  const data = await response.json()
  stores.value = data.stores
})
</script>
```

### Pattern 2: Handle Loading and Error States
```vue
<script setup>
const stores = ref([])
const loading = ref(false)
const error = ref(null)

const loadData = async () => {
  loading.value = true
  error.value = null
  
  try:
    const response = await fetch('/api/sales/getStoreSales/')
    if (!response.ok) throw new Error('Failed to fetch')
    const data = await response.json()
    stores.value = data.stores
  except (err) {
    error.value = err.message
  } finally {
    loading.value = false
  }
}
</script>
```

### Pattern 3: Service Method Pattern
```python
class SalesService:
    def get_all(self):
        # Get all data
        return self.dao.get_all()
    
    def get_sorted(self, sort_by, direction):
        data = self.get_all()
        # Sort and return
        return sorted_data
```

### Pattern 4: Error Handling in Views
```python
@api_view(['GET'])
def get_store_sales(request):
    try:
        service = SalesService()
        data = service.get_all_store_sales()
        return Response(data)
    except Exception as e:
        return Response(
            {'error': str(e)},
            status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )
```

---

## Next Steps

1. **Start with simple examples** - Get one feature working end-to-end
2. **Understand the data flow** - Trace how data moves from JSON → Service → View → Component
3. **Practice with Python** - Learn basic syntax and file operations
4. **Learn Vue.js basics** - Understand reactive data, directives, lifecycle hooks
5. **Build incrementally** - Add one feature at a time

---

## Resources

- **Django Documentation**: https://docs.djangoproject.com/
- **Django REST Framework**: https://www.django-rest-framework.org/
- **Vue.js Documentation**: https://vuejs.org/
- **Python Documentation**: https://docs.python.org/
- **Tailwind CSS**: https://tailwindcss.com/
- **[FRONTEND.md](./FRONTEND.md)** - Detailed frontend documentation (PostCSS, Tailwind CSS, Vue.js patterns)

---

This architecture maintains the same separation of concerns as the Boxlang/ColdBox application while using Django/Python/Vue.js patterns. The concepts are the same, just implemented with different technologies!

For more detailed frontend information including PostCSS setup, Tailwind CSS configuration, and Vue.js component patterns, see [FRONTEND.md](./FRONTEND.md).

