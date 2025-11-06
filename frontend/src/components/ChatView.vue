<template>
  <div class="h-full flex flex-col">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold">Chat History</h2>
      <button 
        @click="$emit('clear-chat')" 
        class="flex items-center space-x-2 text-gray-600 hover:text-gray-800 transition-colors"
      >
        <svg xmlns="http://www.w3.org/2000/svg" class="h-5 w-5" fill="none" viewBox="0 0 24 24" stroke="currentColor">
          <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 7l-.867 12.142A2 2 0 0116.138 21H7.862a2 2 0 01-1.995-1.858L5 7m5 4v6m4-6v6m1-10V4a1 1 0 00-1-1h-4a1 1 0 00-1 1v3M4 7h16" />
        </svg>
        <span>Clear Chat</span>
      </button>
    </div>
    <div class="flex-1 overflow-y-auto space-y-4">
      <div 
        v-for="(chat, index) in chatHistory" 
        :key="index"
        :class="{
          'bg-blue-50 border-blue-200': chat.type === 'user',
          'bg-green-50 border-green-200': chat.type === 'bot',
          'bg-red-50 border-red-200': chat.type === 'error'
        }"
        class="rounded-lg p-4 border"
      >
        <div class="flex justify-between items-center mb-2">
          <span class="font-semibold">
            {{ chat.type === 'user' ? 'You' : (chat.type === 'bot' ? chat.agent : 'System') }}
          </span>
          <span class="text-sm text-gray-500">
            {{ new Date(chat.timestamp).toLocaleTimeString() }}
          </span>
        </div>
        <p class="text-gray-700">
          {{ chat.type === 'error' ? chat.message : chat.response }}
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  chatHistory: Array,
  selectedAgent: String,
  isProcessing: Boolean
})

defineEmits(['clear-chat'])
</script>

