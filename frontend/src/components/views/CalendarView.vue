<template>
  <div class="h-full flex flex-col">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold">Promo Calendar</h2>
      <button 
        @click="loadCalendarData()" 
        class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600"
      >
        Refresh
      </button>
    </div>

    <div class="flex-1 overflow-auto">
      <div v-if="loading" class="flex justify-center items-center h-full">
        <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
      </div>

      <div v-else-if="calendarData" class="bg-white rounded-lg shadow">
        <!-- Calendar Header -->
        <div class="px-6 py-4 border-b">
          <h3 class="text-xl font-semibold text-gray-800">
            {{ calendarData.monthName }} {{ calendarData.year }}
          </h3>
        </div>

        <!-- Calendar Grid -->
        <div class="grid grid-cols-7 gap-px bg-gray-200">
          <!-- Day Headers -->
          <div 
            v-for="day in ['Sun', 'Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat']" 
            :key="day"
            class="bg-gray-50 p-2 text-center text-sm font-medium text-gray-500"
          >
            {{ day }}
          </div>

          <!-- Calendar Days -->
          <div 
            v-for="day in calendarData.days" 
            :key="day.date"
            class="bg-white p-2 min-h-[100px] relative cursor-pointer hover:bg-gray-50 transition-colors"
            :class="{ 'bg-blue-50': day.isToday }"
            @click="selectedDate = day.date"
          >
            <span class="text-sm font-medium">{{ day.day }}</span>
            
            <!-- Events -->
            <div class="mt-1 space-y-1">
              <div 
                v-for="event in getEventsForDate(day.date)" 
                :key="event.date + event.title"
                class="text-xs p-1 rounded cursor-pointer"
                :class="getEventTypeClass(event.type)"
                @click.stop="selectedEvent = event"
              >
                <span>{{ event.title }}</span>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>

    <!-- Event Details Modal -->
    <div 
      v-if="selectedEvent" 
      class="fixed inset-0 bg-black bg-opacity-50 flex items-center justify-center z-50"
      @click.self="selectedEvent = null"
    >
      <div class="bg-white rounded-lg p-6 max-w-md w-full mx-4">
        <div class="flex justify-between items-start mb-4">
          <h3 class="text-lg font-semibold">{{ selectedEvent.title }}</h3>
          <button 
            @click="selectedEvent = null" 
            class="text-gray-500 hover:text-gray-700"
          >
            <svg class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
            </svg>
          </button>
        </div>
        <p class="text-gray-600 mb-4">{{ selectedEvent.description }}</p>
        <div class="text-sm text-gray-500">{{ formatDate(selectedEvent.date) }}</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { fetchCalendarData } from '@/services/api'

const emit = defineEmits(['go-back'])

const currentDate = ref(new Date())
const calendarData = ref(null)
const loading = ref(true)
const selectedDate = ref(null)
const selectedEvent = ref(null)

const loadCalendarData = async () => {
  loading.value = true
  try {
    calendarData.value = await fetchCalendarData()
  } catch (error) {
    console.error('Error loading calendar data:', error)
  } finally {
    loading.value = false
  }
}

const getEventsForDate = (date) => {
  if (!calendarData.value || !calendarData.value.events) return []
  return calendarData.value.events.filter(event => event.date === date)
}

const formatDate = (date) => {
  return new Date(date).toLocaleDateString('en-US', {
    weekday: 'long',
    year: 'numeric',
    month: 'long',
    day: 'numeric'
  })
}

const getEventTypeClass = (type) => {
  switch(type) {
    case 'meeting':
      return 'bg-blue-100 text-blue-800'
    case 'task':
      return 'bg-yellow-100 text-yellow-800'
    case 'promo':
      return 'bg-green-100 text-green-800'
    default:
      return 'bg-gray-100 text-gray-800'
  }
}

onMounted(() => {
  loadCalendarData()
})
</script>
