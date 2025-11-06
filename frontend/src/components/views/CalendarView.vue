<template>
  <div class="h-full flex flex-col">
    <div class="flex justify-end items-center mb-4">
      <button @click="$emit('go-back')" class="flex items-center space-x-2 text-gray-600 hover:text-gray-800">
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 17l-5-5m0 0l5-5m-5 5h12" />
        </svg>
        <span>Go Back</span>
      </button>
    </div>
    <div class="flex-1 overflow-auto">
      <h2 class="text-2xl font-bold mb-4">Promo Calendar</h2>
      <div class="bg-white rounded-lg shadow p-6">
        <p class="text-gray-600">Calendar view coming soon...</p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineEmits(['go-back'])
</script>

