# Frontend Documentation - Vue.js + Tailwind CSS

## Overview

This document explains the frontend architecture, setup, and key concepts for developers working with Vue.js and Tailwind CSS in this project.

---

## Table of Contents

1. [Why PostCSS is Needed](#why-postcss-is-needed)
2. [How Tailwind CSS Works](#how-tailwind-css-works)
3. [Frontend Architecture](#frontend-architecture)
4. [Vue.js Concepts Explained](#vuejs-concepts-explained)
5. [Component Structure](#component-structure)
6. [State Management](#state-management)
7. [API Integration](#api-integration)
8. [Styling with Tailwind CSS](#styling-with-tailwind-css)
9. [Development Workflow](#development-workflow)

---

## Why PostCSS is Needed

### What is PostCSS?

**PostCSS** is a tool that transforms CSS with JavaScript plugins. It's like a "compiler" for CSS that processes your CSS files before they're used in the browser.

### Why Do We Need It for Tailwind CSS?

Tailwind CSS doesn't work directly in the browser. It needs PostCSS to:

1. **Process `@tailwind` Directives**
   - When you write `@tailwind base;` in your CSS file, PostCSS processes these special directives
   - These directives tell Tailwind what to include in the final CSS

2. **Scan Your Code**
   - PostCSS scans all your Vue components, HTML, and JavaScript files
   - It finds which Tailwind classes you're actually using (like `bg-blue-500`, `text-center`, etc.)

3. **Generate Optimized CSS**
   - Instead of including ALL of Tailwind's classes (which would be huge - ~3MB+), it only includes the classes you use
   - This results in a much smaller CSS file (typically 10-50KB)

4. **Apply Autoprefixer**
   - Adds vendor prefixes (`-webkit-`, `-moz-`, etc.) for browser compatibility
   - Ensures your styles work across all browsers

### The Processing Pipeline

```
┌─────────────────────────────────────┐
│  Your CSS File (style.css)           │
│  @tailwind base;                    │
│  @tailwind components;              │
│  @tailwind utilities;                │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  PostCSS Processes                   │
│  - Reads @tailwind directives        │
│  - Scans your Vue components         │
│  - Finds used Tailwind classes       │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Tailwind CSS Plugin                 │
│  - Generates CSS for used classes    │
│  - Applies your custom theme         │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Autoprefixer Plugin                 │
│  - Adds browser prefixes             │
│  - Ensures cross-browser support     │
└──────────────┬──────────────────────┘
               │
               ▼
┌─────────────────────────────────────┐
│  Final Optimized CSS File            │
│  (Only classes you use - ~50KB)     │
└──────────────────────────────────────┘
```

### Example: Without PostCSS vs With PostCSS

**Without PostCSS (CDN approach - what original Boxlang app used):**
```html
<!-- Loads ALL Tailwind classes (~3MB) -->
<script src="https://cdn.tailwindcss.com"></script>
```
- ✅ Simple setup
- ❌ Large file size
- ❌ Runtime compilation (slower)
- ❌ No optimization

**With PostCSS (Build-time approach - what we use):**
```javascript
// postcss.config.js
export default {
  plugins: {
    tailwindcss: {},    // Processes Tailwind
    autoprefixer: {},   // Adds browser prefixes
  },
}
```
- ✅ Optimized file size (only used classes)
- ✅ Build-time compilation (faster)
- ✅ Better performance
- ✅ Full customization

---

## How Tailwind CSS Works

### Tailwind CSS v3 vs v4

**We're using Tailwind CSS v3.4.0** (stable version)

**Tailwind CSS v3:**
- Uses PostCSS plugin: `tailwindcss`
- Configuration: `tailwind.config.js`
- CSS directives: `@tailwind base;`, `@tailwind components;`, `@tailwind utilities;`
- Stable, widely used, excellent documentation

**Tailwind CSS v4:**
- Uses PostCSS plugin: `@tailwindcss/postcss` (separate package)
- Different configuration approach
- Newer, but less stable and different architecture

**Why we use v3:**
- More stable and battle-tested
- Better documentation and community support
- Easier to configure
- Works seamlessly with PostCSS

### Tailwind CSS Configuration

**File: `tailwind.config.js`**
```javascript
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        // Custom colors matching original app
        primary: {
          50: '#f0f9ff',
          500: '#3b82f6',
          900: '#1e40af',
        },
      },
    },
  },
  plugins: [],
}
```

**What this does:**
- `content`: Tells Tailwind which files to scan for classes
- `theme.extend`: Customizes Tailwind's default theme (colors, spacing, etc.)
- `plugins`: Add Tailwind plugins if needed

### Using Tailwind Classes

**In Vue Components:**
```vue
<template>
  <div class="bg-blue-500 text-white p-4 rounded-lg">
    <h2 class="text-2xl font-bold mb-2">Title</h2>
    <p class="text-sm">Content</p>
  </div>
</template>
```

**What happens:**
1. You write `class="bg-blue-500"` in your component
2. PostCSS scans your component and finds this class
3. Tailwind generates CSS for `bg-blue-500` (background color blue)
4. Only this class is included in the final CSS file

---

## Frontend Architecture

### Technology Stack

- **Vue.js 3**: Progressive JavaScript framework
- **Vite**: Fast build tool and dev server
- **Tailwind CSS v3**: Utility-first CSS framework
- **PostCSS**: CSS processor
- **Autoprefixer**: Browser compatibility

### Project Structure

```
frontend/
├── src/
│   ├── main.js              # Vue app entry point
│   ├── App.vue              # Main SPA container (4-panel layout)
│   ├── style.css            # Tailwind directives + custom CSS
│   ├── components/          # Vue components
│   │   ├── LeftPanel.vue   # Left navigation panel
│   │   ├── RightPanel.vue  # Right navigation panel
│   │   ├── ChatView.vue    # Chat interface
│   │   └── views/          # View components
│   │       ├── SalesView.vue
│   │       ├── DeliveriesView.vue
│   │       └── ...
│   └── services/            # API service layer
│       └── api.js           # API client
├── index.html               # HTML entry point
├── vite.config.js           # Vite configuration
├── tailwind.config.js        # Tailwind CSS configuration
├── postcss.config.js        # PostCSS configuration
└── package.json             # Dependencies
```

### 4-Panel Layout

The application uses a **4-panel layout** matching the original Boxlang app:

```
┌──────────┬──────────────────────────┬──────────┐
│          │                          │          │
│  Left    │      Middle Panel        │  Right   │
│  Panel   │      (Main Content)      │  Panel   │
│          │                          │          │
│  Reports │  - Sales View            │  Code    │
│  Section │  - Deliveries View       │  Red/    │
│  (Sky/   │  - Chat View             │  Green   │
│  Blue)   │  - Other Views           │  Section │
│          │                          │  (Red/   │
│  Virtual │                          │  Green)  │
│  Agent   │                          │          │
│  Chat    │                          │  Promos  │
│  (Blue/  │                          │  Section │
│  Indigo) │                          │  (Purple/│
│          │                          │  Pink)   │
└──────────┴──────────────────────────┴──────────┘
```

---

## Vue.js Concepts Explained

### Composition API (What We Use)

**We use `<script setup>` syntax** - the modern Vue 3 way:

```vue
<script setup>
import { ref, onMounted } from 'vue'

// Reactive data
const stores = ref([])
const loading = ref(false)

// Lifecycle hook
onMounted(async () => {
  loading.value = true
  // Fetch data...
  loading.value = false
})
</script>
```

**Key Concepts:**

1. **`ref()` - Reactive References**
   ```javascript
   const stores = ref([])      // Create reactive reference
   stores.value = [...]         // Access/modify with .value
   ```
   - Makes data reactive (UI updates when data changes)
   - Use `.value` to access/modify the value

2. **`onMounted()` - Lifecycle Hook**
   ```javascript
   onMounted(() => {
     // Runs when component is mounted (like componentDidMount in React)
     loadData()
   })
   ```
   - Runs code after component is added to DOM
   - Perfect for fetching data on page load

3. **Template Directives**
   ```vue
   <!-- v-if: Conditional rendering -->
   <div v-if="loading">Loading...</div>
   
   <!-- v-for: Loop through array -->
   <tr v-for="store in stores" :key="store.storeName">
   
   <!-- v-model: Two-way data binding -->
   <input v-model="question">
   
   <!-- :class: Bind classes -->
   <div :class="{ active: isActive }">
   ```

### Component Communication

**Parent to Child (Props):**
```vue
<!-- Parent Component -->
<SalesView :stores="stores" :loading="loading" />

<!-- Child Component -->
<script setup>
defineProps({
  stores: Array,
  loading: Boolean
})
</script>
```

**Child to Parent (Events):**
```vue
<!-- Child Component -->
<button @click="$emit('go-back')">Go Back</button>

<!-- Parent Component -->
<SalesView @go-back="goBack" />
```

---

## Component Structure

### Main App Component (`App.vue`)

**Responsibilities:**
- Manages global state (current view, data, loading states)
- Handles view switching
- Coordinates data loading
- Manages chat functionality

**State Management:**
```javascript
const currentView = ref('weeklyevents')  // Current view
const stores = ref([])                    // Sales data
const loading = ref(false)                // Loading state
const chatHistory = ref([])               // Chat messages
```

### Panel Components

**LeftPanel.vue:**
- Reports section (Sky/Blue theme)
- Virtual Agent chat interface (Blue/Indigo theme)
- Navigation menu items
- Emits events for view switching and data loading

**RightPanel.vue:**
- Code Red/Green section (Red/Green theme)
- Promos per Store section (Purple/Pink theme)
- Navigation menu items

### View Components

**Each view component:**
- Displays data in tables or lists
- Handles loading and error states
- Implements sorting (where applicable)
- Emits events for navigation

**Example: SalesView.vue**
```vue
<template>
  <div class="h-full flex flex-col">
    <button @click="$emit('go-back')">Go Back</button>
    <table>
      <tr v-for="store in stores" :key="store.storeName">
        <td>{{ store.storeName }}</td>
        <td>{{ formatCurrency(store.currentSales) }}</td>
      </tr>
    </table>
  </div>
</template>
```

---

## State Management

### Current Approach: Local State

**We use Vue's `ref()` for state management:**

```javascript
// In App.vue
const currentView = ref('weeklyevents')
const stores = ref([])
const loading = ref(false)
```

**Pros:**
- Simple and straightforward
- No additional dependencies
- Easy to understand

**Cons:**
- State is only in App.vue
- Can get complex with many views

### Future: Pinia (Optional)

If state becomes complex, we can migrate to **Pinia** (Vue's official state management):

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

**For now:** Local state is sufficient. We can migrate to Pinia later if needed.

---

## API Integration

### API Service Layer (`services/api.js`)

**Purpose:**
- Centralized API calls
- Consistent error handling
- Easy to update API endpoints

**Structure:**
```javascript
const API_BASE_URL = '/api'  // Proxied through Vite

async function apiFetch(endpoint, options = {}) {
  const response = await fetch(`${API_BASE_URL}${endpoint}`, {
    headers: { 'Content-Type': 'application/json' },
    ...options
  })
  return await response.json()
}

export async function fetchSalesData() {
  return apiFetch('/sales/getStoreSales/')
}
```

### Vite Proxy Configuration

**File: `vite.config.js`**
```javascript
export default defineConfig({
  server: {
    proxy: {
      '/api': {
        target: 'http://localhost:8000',  // Django backend
        changeOrigin: true,
      },
    },
  },
})
```

**What this does:**
- When frontend makes request to `/api/sales/getStoreSales/`
- Vite proxies it to `http://localhost:8000/api/sales/getStoreSales/`
- Avoids CORS issues during development

### Using API Services in Components

```vue
<script setup>
import { fetchSalesData } from '@/services/api'
import { ref, onMounted } from 'vue'

const stores = ref([])
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const data = await fetchSalesData()
    stores.value = data.stores
  } catch (error) {
    console.error('Error:', error)
  } finally {
    loading.value = false
  }
})
</script>
```

---

## Styling with Tailwind CSS

### Utility-First Approach

**Instead of writing custom CSS:**
```css
/* ❌ Old way */
.my-button {
  background-color: blue;
  color: white;
  padding: 8px 16px;
  border-radius: 4px;
}
```

**Use Tailwind utility classes:**
```vue
<!-- ✅ Tailwind way -->
<button class="bg-blue-500 text-white px-4 py-2 rounded">
  Click me
</button>
```

### Common Tailwind Patterns

**Colors:**
```vue
<div class="bg-blue-500 text-white">        <!-- Background & text color -->
<div class="border-blue-200">               <!-- Border color -->
<div class="text-gray-800">                 <!-- Text color -->
```

**Spacing:**
```vue
<div class="p-4">                           <!-- Padding: 1rem -->
<div class="m-2">                           <!-- Margin: 0.5rem -->
<div class="px-6 py-3">                     <!-- Padding X & Y -->
```

**Layout:**
```vue
<div class="flex items-center">             <!-- Flexbox -->
<div class="grid grid-cols-3 gap-4">        <!-- Grid -->
<div class="w-1/5">                         <!-- Width: 20% -->
```

**Responsive:**
```vue
<div class="text-sm md:text-base lg:text-lg">  <!-- Responsive text size -->
<div class="hidden md:block">                   <!-- Hide on mobile, show on desktop -->
```

### Matching Original App Colors

**Left Panel - Reports Section (Sky/Blue):**
```vue
<div class="bg-gradient-to-r from-sky-100 to-blue-100 border border-sky-200">
  <h3 class="text-sky-800">Reports</h3>
</div>
```

**Right Panel - Code Red/Green (Red/Green):**
```vue
<div class="bg-gradient-to-r from-red-100 to-green-100 border border-red-200">
  <h3 class="text-red-800">Code Red/Green</h3>
</div>
```

**Right Panel - Promos (Purple/Pink):**
```vue
<div class="bg-gradient-to-r from-purple-100 to-pink-100 border border-purple-200">
  <h3 class="text-purple-800">Promos per Store</h3>
</div>
```

---

## Development Workflow

### Running the Frontend

```bash
cd frontend
npm install          # Install dependencies (first time only)
npm run dev          # Start development server
```

**Development server:**
- Runs on `http://localhost:5173`
- Hot Module Replacement (HMR) - changes update automatically
- Proxies `/api` requests to Django backend

### Building for Production

```bash
npm run build        # Build optimized production files
npm run preview      # Preview production build locally
```

**What happens during build:**
1. PostCSS processes Tailwind CSS
2. Only used classes are included
3. CSS is minified and optimized
4. JavaScript is bundled and optimized
5. Files are output to `dist/` directory

### File Changes and Hot Reload

**Vite automatically:**
- Detects file changes
- Recompiles only changed files
- Updates browser without full page reload
- Preserves component state when possible

---

## Common Patterns

### Pattern 1: Loading Data on Mount

```vue
<script setup>
import { ref, onMounted } from 'vue'
import { fetchSalesData } from '@/services/api'

const stores = ref([])
const loading = ref(false)

onMounted(async () => {
  loading.value = true
  try {
    const data = await fetchSalesData()
    stores.value = data.stores
  } catch (error) {
    console.error('Error:', error)
  } finally {
    loading.value = false
  }
})
</script>
```

### Pattern 2: Conditional Rendering

```vue
<template>
  <div v-if="loading" class="flex items-center justify-center">
    <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
  </div>
  
  <div v-else-if="error" class="text-red-500">
    Error: {{ error }}
  </div>
  
  <div v-else>
    <!-- Content -->
  </div>
</template>
```

### Pattern 3: Table with Sorting

```vue
<template>
  <table>
    <thead>
      <tr>
        <th 
          class="cursor-pointer hover:bg-gray-100"
          @click="$emit('sort', 'storeName')"
        >
          Store Name
        </th>
      </tr>
    </thead>
    <tbody>
      <tr v-for="store in stores" :key="store.storeName">
        <td>{{ store.storeName }}</td>
      </tr>
    </tbody>
  </table>
</template>
```

### Pattern 4: Formatting Functions

```vue
<script setup>
const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD',
    minimumFractionDigits: 0
  }).format(value)
}

const formatNumber = (value) => {
  return new Intl.NumberFormat('en-US').format(value)
}
</script>

<template>
  <div>{{ formatCurrency(store.currentSales) }}</div>
</template>
```

---

## Troubleshooting

### PostCSS/Tailwind Errors

**Error: "PostCSS plugin not found"**
- Solution: Make sure `tailwindcss` and `postcss` are installed
- Run: `npm install -D tailwindcss@3.4.0 postcss autoprefixer`

**Error: "It looks like you're trying to use `tailwindcss` directly as a PostCSS plugin"**
- **Cause:** This error occurs when Tailwind CSS v4 is installed (which requires `@tailwindcss/postcss`)
- **Solution:** Use Tailwind CSS v3.4.0 instead:
  ```bash
  npm uninstall tailwindcss @tailwindcss/postcss
  npm install -D tailwindcss@3.4.0 postcss autoprefixer
  ```
- **Verify:** Check `package.json` shows `"tailwindcss": "^3.4.0"` (not `^4.x.x`)
- **PostCSS Config:** Use ES module format in `postcss.config.js` (since `package.json` has `"type": "module"`):
  ```javascript
  export default {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  }
  ```
  **Note:** If your project uses CommonJS (no `"type": "module"` in `package.json`), use:
  ```javascript
  module.exports = {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  }
  ```
- **Clear Cache:** Remove Vite cache and restart:
  ```bash
  rm -rf node_modules/.vite dist .vite
  npm run dev
  ```

**Error: "module is not defined in ES module scope"**
- **Cause:** Using CommonJS syntax (`module.exports`) in a project with `"type": "module"` in `package.json`
- **Solution:** Use ES module syntax (`export default`) in `postcss.config.js`:
  ```javascript
  export default {
    plugins: {
      tailwindcss: {},
      autoprefixer: {},
    },
  }
  ```

**Error: "Tailwind classes not working"**
- Check: `tailwind.config.js` - make sure `content` paths are correct
- Check: `style.css` - make sure `@tailwind` directives are present
- Check: `postcss.config.js` - make sure `tailwindcss` plugin is configured
- Clear Vite cache: `rm -rf node_modules/.vite` and restart server

### API Connection Issues

**Error: "Failed to fetch" or CORS errors**
- Check: Django server is running on `http://localhost:8000`
- Check: `vite.config.js` has proxy configuration
- Check: API endpoints are correct in `services/api.js`

**Error: "404 Not Found"**
- Check: Django URL routing in `app/urls.py`
- Check: API endpoint paths match between frontend and backend

### Vue Component Errors

**Error: "Component not found"**
- Check: Import path is correct
- Check: Component file exists
- Check: Component is exported correctly

**Error: "Cannot read property of undefined"**
- Check: Data is loaded before accessing properties
- Use optional chaining: `store?.storeName`
- Add loading states

---

## Key Takeaways

1. **PostCSS is essential** - It processes Tailwind CSS and generates optimized CSS
2. **Tailwind v3 is stable** - We use v3.4.0 for reliability
3. **Vite proxies API calls** - Avoids CORS issues during development
4. **Vue Composition API** - Modern Vue 3 syntax with `<script setup>`
5. **Component-based architecture** - Each view is a separate component
6. **Utility-first CSS** - Use Tailwind classes instead of custom CSS
7. **4-panel layout** - Matches original Boxlang app design

---

## Resources

- **Vue.js Documentation**: https://vuejs.org/
- **Tailwind CSS Documentation**: https://tailwindcss.com/docs
- **Vite Documentation**: https://vite.dev/
- **PostCSS Documentation**: https://postcss.org/
- **Vue Composition API Guide**: https://vuejs.org/guide/extras/composition-api-faq.html

---

This frontend architecture provides a clean, maintainable, and performant foundation for the restaurant manager dashboard application.

