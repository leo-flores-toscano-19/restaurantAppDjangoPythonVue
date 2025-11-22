<template>
  <div class="w-1/5 bg-gray-100 flex flex-col h-full min-h-screen px-4">
    <div class="flex-1 flex flex-col p-4 overflow-y-auto">
      <!-- Code Red/Green Section (Red/Green theme) -->
      <div class="bg-gradient-to-r from-red-100 to-green-100 rounded-lg p-4 mb-4 border border-red-200">
        <h3 class="text-lg font-semibold mb-3 text-red-800">Code Red/Green</h3>
        <ul class="space-y-2">
          <li 
            class="flex items-center space-x-2 hover:bg-red-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-critical-issues')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-red-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            <span class="text-red-800">Critical Issues</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-green-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-feedback')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-green-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="text-green-800">Positive Feedback</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-yellow-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-response-time')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-yellow-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4l3 3m6-3a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="text-yellow-800">Response Time</span>
          </li>
        </ul>
      </div>

      <!-- Promos per Store Section (Purple/Pink theme) -->
      <div class="bg-gradient-to-r from-purple-100 to-pink-100 rounded-lg p-4 mb-4 border border-purple-200">
        <h3 class="text-lg font-semibold mb-3 text-purple-800">Promos per Store</h3>
        <ul class="space-y-2">
          <li 
            class="flex items-center space-x-2 hover:bg-purple-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-promotions')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-purple-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="text-purple-800">Active Promotions</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-pink-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-calendar')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-pink-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5H7a2 2 0 00-2 2v12a2 2 0 002 2h10a2 2 0 002-2V7a2 2 0 00-2-2h-2M9 5a2 2 0 002 2h2a2 2 0 002-2M9 5a2 2 0 012-2h2a2 2 0 012 2" />
            </svg>
            <span class="text-pink-800">Promo Calendar</span>
          </li>
        </ul>
      </div>

      <!-- About This App Section (Teal/Cyan theme) -->
      <div class="bg-gradient-to-r from-teal-100 to-cyan-100 rounded-lg p-4 mb-4 border border-teal-200">
        <h3 class="text-lg font-semibold mb-3 text-teal-800">About This App</h3>
        <ul class="space-y-2">
          <li 
            class="flex items-center space-x-2 hover:bg-teal-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-tech-stack')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-teal-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9.663 17h4.673M12 3v1m6.364 1.636l-.707.707M21 12h-1M4 12H3m3.343-5.657l-.707-.707m2.828 9.9a5 5 0 117.072 0l-.548.547A3.374 3.374 0 0014 18.469V19a2 2 0 11-4 0v-.531c0-.895-.356-1.754-.988-2.386l-.548-.547z" />
            </svg>
            <span class="text-teal-800">Technology Stack</span>
          </li>
        </ul>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['set-view', 'load-critical-issues', 'load-feedback', 'load-response-time', 'load-promotions', 'load-calendar', 'load-tech-stack'])
</script>

