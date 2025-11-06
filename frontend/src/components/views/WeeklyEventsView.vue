<template>
  <div class="h-full flex flex-col">
    <div v-if="loading" class="flex items-center justify-center h-full">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>
    <div v-else class="flex-1 overflow-auto">
      <h2 class="text-2xl font-bold mb-4">Weekly Events</h2>
      <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
        <div 
          v-for="event in events" 
          :key="event.id"
          class="bg-white rounded-lg shadow p-4 border-l-4"
          :class="{
            'border-blue-500': event.color === 'blue',
            'border-green-500': event.color === 'green',
            'border-red-500': event.color === 'red',
            'border-yellow-500': event.color === 'yellow'
          }"
        >
          <h3 class="font-semibold text-lg mb-2">{{ event.title }}</h3>
          <p class="text-gray-600 text-sm mb-2">{{ event.description }}</p>
          <div class="flex items-center space-x-2 text-sm text-gray-500">
            <span>{{ event.date }}</span>
            <span>•</span>
            <span>{{ event.time }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  events: Array,
  loading: Boolean
})
</script>

