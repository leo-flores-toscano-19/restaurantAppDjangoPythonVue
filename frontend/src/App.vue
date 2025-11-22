<template>
  <div class="h-screen w-screen flex overflow-hidden bg-gray-50">
    <!-- Left Panel - Reports Section (Sky/Blue theme) -->
    <LeftPanel 
      :current-view="currentView"
      @set-view="setView"
      @load-sales="loadSalesData"
      @load-deliveries="loadDeliveriesData"
      @load-pos-issues="loadPosIssuesData"
      @load-performance="loadPerformanceData"
      @load-feedback="loadFeedbackData"
      @load-response-time="loadResponseTimeData"
      @chat-message="handleChatMessage"
      @chat-response="handleChatResponse"
    />

    <!-- Middle Panel - Main Content Area -->
    <div class="flex-1 bg-white p-6 overflow-hidden flex flex-col min-h-screen">
      <div class="h-full flex flex-col">
        <!-- Chat View -->
        <ChatView 
          v-if="currentView === 'chat'"
          :chat-history="chatHistory"
          :selected-agent="selectedAgent"
          :is-processing="isProcessing"
          @clear-chat="clearChat"
        />

        <!-- Sales View -->
        <SalesView 
          v-if="currentView === 'sales'"
          :stores="stores"
          :loading="loading"
          @go-back="goBack"
          @sort="sortSales"
        />

        <!-- Deliveries View -->
        <DeliveriesView 
          v-if="currentView === 'deliveries'"
          :deliveries="deliveries"
          :loading="loading"
          @go-back="goBack"
          @sort="sortDeliveries"
        />

        <!-- POS Issues View -->
        <PosIssuesView 
          v-if="currentView === 'posIssues'"
          :pos-issues="posIssues"
          :loading="loading"
          @go-back="goBack"
          @sort="sortPosIssues"
        />

        <!-- Performance View -->
        <PerformanceView 
          v-if="currentView === 'performance'"
          :stores="stores"
          :loading="loading"
          @go-back="goBack"
          @sort="sortPerformance"
        />

        <!-- Feedback View -->
        <PositiveFeedbackView 
          v-if="currentView === 'feedback'"
          :feedback="feedback"
          :loading="loading"
          @go-back="goBack"
          @sort="sortFeedback"
        />

        <!-- Response Time View -->
        <ResponseTimeView 
          v-if="currentView === 'response'"
          :responses="responses"
          :loading="loading"
          @go-back="goBack"
        />

        <!-- Weekly Events View (Default) -->
        <WeeklyEventsView 
          v-if="currentView === 'weeklyevents'"
          :events="weeklyEvents"
          :loading="loading"
        />

        <!-- Critical Issues View -->
        <CriticalIssuesView 
          v-if="currentView === 'criticalissues'"
          :issues="criticalIssues"
          :loading="loading"
          @go-back="goBack"
        />

        <!-- Promotions View -->
        <PromotionsView 
          v-if="currentView === 'promotions'"
          :promotions="promotions"
          :loading="loading"
          @go-back="goBack"
          @sort="sortPromotions"
        />

        <!-- Calendar View -->
        <CalendarView 
          v-if="currentView === 'calendar'"
          @go-back="goBack"
        />

        <!-- Tech Stack View -->
        <TechStackView 
          v-if="currentView === 'techstack'"
          @go-back="goBack"
        />
      </div>
    </div>

    <!-- Right Panel - Code Red/Green + Promos per Store (Red/Green + Purple/Pink themes) -->
    <RightPanel 
      :current-view="currentView"
      @set-view="setView"
      @load-critical-issues="loadCriticalIssuesData"
      @load-feedback="loadFeedbackData"
      @load-response-time="loadResponseTimeData"
      @load-promotions="loadPromotionsData"
      @load-calendar="setView('calendar')"
      @load-tech-stack="setView('techstack')"
    />
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import LeftPanel from './components/LeftPanel.vue'
import RightPanel from './components/RightPanel.vue'
import ChatView from './components/ChatView.vue'
import SalesView from './components/views/SalesView.vue'
import DeliveriesView from './components/views/DeliveriesView.vue'
import PosIssuesView from './components/views/PosIssuesView.vue'
import PerformanceView from './components/views/PerformanceView.vue'
import PositiveFeedbackView from './components/views/PositiveFeedbackView.vue'
import ResponseTimeView from './components/views/ResponseTimeView.vue'
import WeeklyEventsView from './components/views/WeeklyEventsView.vue'
import CriticalIssuesView from './components/views/CriticalIssuesView.vue'
import PromotionsView from './components/views/PromotionsView.vue'
import CalendarView from './components/views/CalendarView.vue'
import TechStackView from './components/views/TechStackView.vue'

import { 
  fetchSalesData, 
  fetchSalesSorted,
  fetchDeliveriesData,
  fetchDeliveriesSorted,
  fetchCriticalIssuesData,
  fetchPosIssuesData,
  fetchPosIssuesSorted,
  fetchPromotionsData,
  fetchPerformanceData,
  fetchFeedbackData,
  fetchFeedbackSorted,
  fetchResponseTimeData,
  fetchWeeklyEventsData,
  fetchApplicationIssue,
  fetchTicketStatus,
  fetchConfiguration
} from './services/api'

// State management
const currentView = ref('weeklyevents')
const previousView = ref('weeklyevents')
const loading = ref(false)

// Data state
const stores = ref([])
const deliveries = ref([])
const criticalIssues = ref([])
const posIssues = ref([])
const promotions = ref([])
const feedback = ref([])
const responses = ref([])
const weeklyEvents = ref([])

// Chat state
const chatHistory = ref([])
const selectedAgent = ref('Application Issues')
const isProcessing = ref(false)

// Sorting state
const sortBy = ref('storeName')
const sortDirection = ref('asc')

// View management
const setView = (view) => {
  previousView.value = currentView.value
  currentView.value = view
}

const goBack = () => {
  currentView.value = previousView.value
}

// Data loading functions
const loadSalesData = async () => {
  loading.value = true
  setView('sales')
  try {
    const data = await fetchSalesData()
    stores.value = data.stores || []
  } catch (error) {
    console.error('Error loading sales:', error)
  } finally {
    loading.value = false
  }
}

const loadDeliveriesData = async () => {
  loading.value = true
  setView('deliveries')
  try {
    const data = await fetchDeliveriesData()
    deliveries.value = data.deliveries || []
  } catch (error) {
    console.error('Error loading deliveries:', error)
  } finally {
    loading.value = false
  }
}

const loadCriticalIssuesData = async () => {
  loading.value = true
  setView('criticalissues')
  try {
    const data = await fetchCriticalIssuesData()
    criticalIssues.value = data.issues || []
  } catch (error) {
    console.error('Error loading critical issues:', error)
  } finally {
    loading.value = false
  }
}

const loadPosIssuesData = async () => {
  loading.value = true
  setView('posIssues')
  try {
    const data = await fetchPosIssuesData()
    posIssues.value = data.issues || []
  } catch (error) {
    console.error('Error loading POS issues:', error)
  } finally {
    loading.value = false
  }
}

const loadPromotionsData = async () => {
  loading.value = true
  setView('promotions')
  try {
    const data = await fetchPromotionsData()
    // Promotions API returns the array directly, not wrapped in 'promotions'
    promotions.value = Array.isArray(data) ? data : (data.promotions || [])
  } catch (error) {
    console.error('Error loading promotions:', error)
  } finally {
    loading.value = false
  }
}

const loadPerformanceData = async () => {
  loading.value = true
  setView('performance')
  try {
    const data = await fetchPerformanceData()
    stores.value = data.stores || []
  } catch (error) {
    console.error('Error loading performance:', error)
  } finally {
    loading.value = false
  }
}

const loadFeedbackData = async () => {
  loading.value = true
  setView('feedback')
  try {
    const data = await fetchFeedbackData()
    feedback.value = data.feedback || []
  } catch (error) {
    console.error('Error loading feedback:', error)
  } finally {
    loading.value = false
  }
}

const loadResponseTimeData = async () => {
  loading.value = true
  setView('response')
  try {
    const data = await fetchResponseTimeData()
    responses.value = data.responses || []
  } catch (error) {
    console.error('Error loading response time:', error)
  } finally {
    loading.value = false
  }
}

// Sorting functions
const sortSales = async (column) => {
  if (sortBy.value === column) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = column
    sortDirection.value = 'asc'
  }
  
  try {
    const data = await fetchSalesSorted(sortBy.value, sortDirection.value)
    stores.value = data.stores || []
  } catch (error) {
    console.error('Error sorting sales:', error)
  }
}

const sortDeliveries = async (column) => {
  if (sortBy.value === column) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = column
    sortDirection.value = 'asc'
  }
  
  try {
    const data = await fetchDeliveriesSorted(sortBy.value, sortDirection.value)
    deliveries.value = data.deliveries || []
  } catch (error) {
    console.error('Error sorting deliveries:', error)
  }
}

const sortPosIssues = async ({ column, direction, action }) => {
  if (action === 'reload') {
    try {
      const data = await fetchPosIssuesData()
      posIssues.value = data.issues || []
    } catch (error) {
      console.error('Error reloading POS issues:', error)
    }
    return
  }
  
  sortBy.value = column
  sortDirection.value = direction
  
  try {
    const data = await fetchPosIssuesSorted(column, direction)
    posIssues.value = data.issues || []
  } catch (error) {
    console.error('Error sorting POS issues:', error)
  }
}

const sortFeedback = async (column) => {
  if (sortBy.value === column) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = column
    sortDirection.value = 'asc'
  }
  
  try {
    const data = await fetchFeedbackSorted(sortBy.value, sortDirection.value)
    feedback.value = data.feedback || []
  } catch (error) {
    console.error('Error sorting feedback:', error)
  }
}

const sortPromotions = async ({ column, direction }) => {
  sortBy.value = column
  sortDirection.value = direction
  
  try {
    const data = await fetchPromotionsSorted(column, direction)
    // Promotions API returns the array directly, not wrapped in 'promotions'
    promotions.value = Array.isArray(data) ? data : (data.promotions || [])
  } catch (error) {
    console.error('Error sorting promotions:', error)
  }
}

const sortPerformance = async ({ column, direction }) => {
  sortBy.value = column
  sortDirection.value = direction
  
  try {
    const data = await fetchPerformanceSorted(column, direction)
    stores.value = data.stores || []
  } catch (error) {
    console.error('Error sorting performance:', error)
  }
}

// Chat functions
const clearChat = () => {
  chatHistory.value = []
}

const handleChatMessage = (message) => {
  chatHistory.value.push(message)
  setView('chat')
}

const handleChatResponse = (response) => {
  chatHistory.value.push(response)
}

// Load initial data
onMounted(async () => {
  try {
    const data = await fetchWeeklyEventsData()
    weeklyEvents.value = data.events || []
  } catch (error) {
    console.error('Error loading weekly events:', error)
  }
})
</script>
