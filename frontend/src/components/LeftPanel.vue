<template>
  <div class="w-1/5 bg-gray-100 flex flex-col h-full min-h-screen px-4">
    <div class="flex-1 flex flex-col p-4 overflow-y-auto">
      <!-- Top Tile - Reports Section (Sky/Blue theme) -->
      <div class="bg-gradient-to-r from-sky-100 to-blue-100 rounded-lg p-4 mb-4 border border-sky-200">
        <h3 class="text-lg font-semibold mb-3 text-sky-800">Reports</h3>
        <ul class="space-y-2">
          <li 
            class="flex items-center space-x-2 hover:bg-sky-50 p-2 rounded cursor-pointer transition-colors"
            @click="setView('weeklyevents')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-sky-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 7V3m8 4V3m-9 8h10M5 21h14a2 2 0 002-2V7a2 2 0 00-2-2H5a2 2 0 00-2 2v12a2 2 0 002 2z" />
            </svg>
            <span class="text-sky-800">Weekly Events</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-sky-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-sales')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-sky-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8c-1.657 0-3 .895-3 2s1.343 2 3 2 3 .895 3 2-1.343 2-3 2m0-8c1.11 0 2.08.402 2.599 1M12 8V7m0 1v8m0 0v1m0-1c-1.11 0-2.08-.402-2.599-1M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
            </svg>
            <span class="text-sky-800">Sales By Store</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-sky-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-deliveries')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-sky-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 8h14M5 8a2 2 0 110-4h14a2 2 0 110 4M5 8v10a2 2 0 002 2h10a2 2 0 002-2V8m-9 4h4" />
            </svg>
            <span class="text-sky-800">Deliveries</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-sky-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-pos-issues')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-sky-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 9v2m0 4h.01m-6.938 4h13.856c1.54 0 2.502-1.667 1.732-3L13.732 4c-.77-1.333-2.694-1.333-3.464 0L3.34 16c-.77 1.333.192 3 1.732 3z" />
            </svg>
            <span class="text-sky-800">POS Issues</span>
          </li>
          <li 
            class="flex items-center space-x-2 hover:bg-sky-50 p-2 rounded cursor-pointer transition-colors"
            @click="$emit('load-performance')"
          >
            <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5 text-sky-600" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 19v-6a2 2 0 00-2-2H5a2 2 0 00-2 2v6a2 2 0 002 2h2a2 2 0 002-2zm0 0V9a2 2 0 012-2h2a2 2 0 012 2v10m-6 0a2 2 0 002 2h2a2 2 0 002-2m0 0V5a2 2 0 012-2h2a2 2 0 012 2v14a2 2 0 01-2 2h-2a2 2 0 01-2-2z" />
            </svg>
            <span class="text-sky-800">Performance Metrics</span>
          </li>
        </ul>
      </div>

      <!-- Bottom Tile - Virtual Agent (Blue/Indigo theme) -->
      <div class="bg-gradient-to-r from-blue-100 to-indigo-100 rounded-lg p-4 border border-blue-200">
        <h3 class="text-lg font-semibold mb-3 text-blue-800">Virtual Agent</h3>
        <form @submit.prevent="submitQuestion">
          <div class="mb-3">
            <label class="block text-sm font-medium mb-1 text-blue-700">What can I help you with?</label>
            <select 
              v-model="selectedAgent" 
              class="w-full bg-white/50 border border-blue-200 rounded p-2 text-blue-800 focus:ring-2 focus:ring-blue-300 focus:border-blue-300"
            >
              <option value="Application Issues">Application Issues</option>
              <option value="Ticket Status">Ticket Status</option>
              <option value="Help with configuration">Help with configuration</option>
            </select>
          </div>
          <div class="mb-3">
            <label class="block text-sm font-medium mb-1 text-blue-700">Please type your question</label>
            <input 
              type="text" 
              v-model="question" 
              class="w-full bg-white/50 border border-blue-200 rounded p-2 text-blue-800 placeholder-blue-300 focus:ring-2 focus:ring-blue-300 focus:border-blue-300"
              placeholder="Type your question here..."
              :disabled="isProcessing"
            />
          </div>
          <button 
            type="submit" 
            class="w-full bg-gradient-to-r from-blue-500 to-indigo-500 text-white font-semibold py-2 px-4 rounded hover:from-blue-600 hover:to-indigo-600 transition-colors shadow-sm"
            :disabled="isProcessing"
          >
            <span v-if="!isProcessing">Start Chat</span>
            <span v-else class="flex items-center justify-center">
              <svg class="animate-spin -ml-1 mr-3 h-5 w-5 text-white" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
                <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
                <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
              </svg>
              Processing...
            </span>
          </button>
        </form>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { fetchApplicationIssue, fetchTicketStatus, fetchConfiguration } from '../services/api'

const props = defineProps({
  currentView: String
})

const emit = defineEmits(['set-view', 'load-sales', 'load-deliveries', 'load-pos-issues', 'load-performance', 'load-feedback', 'load-response-time', 'chat-message', 'chat-response'])

const selectedAgent = ref('Application Issues')
const question = ref('')
const isProcessing = ref(false)

const setView = (view) => {
  emit('set-view', view)
}

const submitQuestion = async () => {
  if (!question.value.trim()) return
  
  isProcessing.value = true
  setView('chat')
  
  // Emit chat message to parent
  emit('chat-message', {
    type: 'user',
    agent: selectedAgent.value,
    question: question.value,
    timestamp: new Date()
  })
  
  try {
    let response
    const timestamp = Date.now()
    
    // Route to appropriate handler based on selected agent
    if (selectedAgent.value === 'Application Issues') {
      response = await fetchApplicationIssue(question.value)
    } else if (selectedAgent.value === 'Ticket Status') {
      response = await fetchTicketStatus()
    } else if (selectedAgent.value === 'Help with configuration') {
      response = await fetchConfiguration()
    } else {
      response = await fetchApplicationIssue(question.value)
    }
    
    // Emit bot response to parent
    emit('chat-response', {
      type: 'bot',
      agent: selectedAgent.value,
      response: response.response || 'I apologize, but I could not process your request at this time.',
      timestamp: new Date()
    })
  } catch (error) {
    console.error('Error:', error)
    emit('chat-response', {
      type: 'error',
      message: 'Sorry, there was an error processing your request.',
      timestamp: new Date()
    })
  } finally {
    isProcessing.value = false
    question.value = ''
  }
}
</script>

