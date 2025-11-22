<template>
  <div class="h-full flex flex-col">
    <div class="flex justify-end items-center mb-4">
      <button 
        @click="$emit('go-back')" 
        class="flex items-center space-x-2 text-gray-600 hover:text-gray-800 transition-colors"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 17l-5-5m0 0l5-5m-5 5h12" />
        </svg>
        <span>Go Back</span>
      </button>
    </div>
    
    <div class="flex-1 overflow-auto">
      <h2 class="text-3xl font-bold mb-6 text-gray-800">Technology Stack</h2>
      
      <div class="space-y-6">
        <!-- Frontend Technologies -->
        <div class="bg-gradient-to-r from-blue-50 to-indigo-50 rounded-lg p-6 border border-blue-200">
          <h3 class="text-2xl font-semibold mb-4 text-blue-800 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.75 17L9 20l-1 1h8l-1-1-.75-3M3 13h18M5 17h14a2 2 0 002-2V5a2 2 0 00-2-2H5a2 2 0 00-2 2v10a2 2 0 002 2z" />
            </svg>
            Frontend
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Vue.js</h4>
              <p class="text-sm text-gray-600">Version 3.5.22</p>
              <p class="text-sm text-gray-500 mt-1">Progressive JavaScript framework for building user interfaces</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Vite</h4>
              <p class="text-sm text-gray-600">Version 7.1.7</p>
              <p class="text-sm text-gray-500 mt-1">Fast build tool and development server</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Tailwind CSS</h4>
              <p class="text-sm text-gray-600">Version 3.4.0</p>
              <p class="text-sm text-gray-500 mt-1">Utility-first CSS framework for rapid UI development</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">PostCSS</h4>
              <p class="text-sm text-gray-600">Version 8.5.6</p>
              <p class="text-sm text-gray-500 mt-1">CSS processor for transforming styles with JavaScript plugins</p>
            </div>
          </div>
        </div>

        <!-- Backend Technologies -->
        <div class="bg-gradient-to-r from-green-50 to-emerald-50 rounded-lg p-6 border border-green-200">
          <h3 class="text-2xl font-semibold mb-4 text-green-800 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 12h14M5 12a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v4a2 2 0 01-2 2M5 12a2 2 0 00-2 2v4a2 2 0 002 2h14a2 2 0 002-2v-4a2 2 0 00-2-2m-2-4h.01M17 16h.01" />
            </svg>
            Backend
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Django</h4>
              <p class="text-sm text-gray-600">Version 4.2.7</p>
              <p class="text-sm text-gray-500 mt-1">High-level Python web framework for rapid development</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Django REST Framework</h4>
              <p class="text-sm text-gray-600">Version 3.14.0</p>
              <p class="text-sm text-gray-500 mt-1">Powerful toolkit for building Web APIs</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Python</h4>
              <p class="text-sm text-gray-600">Version 3.9+</p>
              <p class="text-sm text-gray-500 mt-1">Programming language for backend development</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Django CORS Headers</h4>
              <p class="text-sm text-gray-600">Version 4.3.1</p>
              <p class="text-sm text-gray-500 mt-1">Handles Cross-Origin Resource Sharing (CORS) for Django</p>
            </div>
          </div>
        </div>

        <!-- Architecture & Patterns -->
        <div class="bg-gradient-to-r from-purple-50 to-pink-50 rounded-lg p-6 border border-purple-200">
          <h3 class="text-2xl font-semibold mb-4 text-purple-800 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
            </svg>
            Architecture & Patterns
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">DAO/Repository Pattern</h4>
              <p class="text-sm text-gray-500 mt-1">Abstract data access layer for easy switching between JSON, PostgreSQL, and MongoDB</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Service Layer</h4>
              <p class="text-sm text-gray-500 mt-1">Business logic separated from data access and presentation layers</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">Component-Based Architecture</h4>
              <p class="text-sm text-gray-500 mt-1">Vue.js components for modular and reusable UI elements</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">RESTful API</h4>
              <p class="text-sm text-gray-500 mt-1">Standard HTTP methods for API communication between frontend and backend</p>
            </div>
          </div>
        </div>

        <!-- Data Storage -->
        <div class="bg-gradient-to-r from-amber-50 to-orange-50 rounded-lg p-6 border border-amber-200">
          <h3 class="text-2xl font-semibold mb-4 text-amber-800 flex items-center">
            <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6 mr-2" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 7v10c0 2.21 3.582 4 8 4s8-1.79 8-4V7M4 7c0 2.21 3.582 4 8 4s8-1.79 8-4M4 7c0-2.21 3.582-4 8-4s8 1.79 8 4m0 5c0 2.21-3.582 4-8 4s-8-1.79-8-4" />
            </svg>
            Data Storage
          </h3>
          <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">JSON Files</h4>
              <p class="text-sm text-gray-500 mt-1">Default data storage (current implementation)</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">PostgreSQL</h4>
              <p class="text-sm text-gray-500 mt-1">Relational database (easily switchable via DAO pattern)</p>
            </div>
            <div class="bg-white rounded-lg p-4 shadow-sm">
              <h4 class="font-semibold text-gray-800 mb-2">MongoDB</h4>
              <p class="text-sm text-gray-500 mt-1">NoSQL database (easily switchable via DAO pattern)</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['go-back'])
</script>









