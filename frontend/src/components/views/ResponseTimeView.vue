<template>
  <div class="h-full flex flex-col p-6 bg-white">
    <div class="mb-6">
      <h2 class="text-2xl font-bold text-gray-800">Response Time Report</h2>
      <p class="text-gray-600">Track and analyze response times for critical issues</p>
    </div>

    <div v-if="loading" class="flex items-center justify-center h-full">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>

    <div v-else class="flex-1 overflow-auto space-y-4">
      <div 
        v-for="response in responses" 
        :key="response.id"
        class="bg-white rounded-lg shadow-sm hover:shadow-md transition-all duration-200 p-4 border-2 border-gray-300"
      >
        <!-- Header Row -->
        <div class="flex items-center justify-between mb-3">
          <div class="flex items-center space-x-6">
            <div>
              <span class="text-sm font-semibold text-gray-500">Store:</span>
              <span class="text-base text-gray-700 ml-2">{{ response.storeName }}</span>
            </div>
            <div>
              <span class="text-sm font-semibold text-gray-500">Module:</span>
              <span class="text-base text-gray-700 ml-2">{{ response.module }}</span>
            </div>
            <div>
              <span class="text-sm font-semibold text-gray-500">Initial Contact:</span>
              <span class="text-base text-gray-700 ml-2">{{ response.initialContactTime }}</span>
            </div>
          </div>
          <div class="flex items-center space-x-3">
            <div>
              <span class="text-sm font-semibold text-gray-500">Status:</span>
              <span class="text-base text-gray-700 ml-2">{{ response.status }}</span>
            </div>
            <div>
              <span class="text-sm font-semibold text-gray-500">Priority:</span>
              <span class="text-base text-gray-700 ml-2">{{ response.priority }}</span>
            </div>
          </div>
        </div>

        <!-- Details Section -->
        <div class="border-t-2 border-gray-300 pt-3 mb-3">
          <div class="grid grid-cols-3 gap-3">
            <div class="border-2 border-gray-200 p-3 rounded-lg">
              <span class="text-sm font-semibold text-gray-500 block mb-2">Complaint</span>
              <p class="text-base text-gray-700">{{ response.complaint }}</p>
            </div>
            <div class="border-2 border-gray-200 p-3 rounded-lg">
              <span class="text-sm font-semibold text-gray-500 block mb-2">Remediation</span>
              <p class="text-base text-gray-700">{{ response.remediationDetails }}</p>
            </div>
            <div class="border-2 border-gray-200 p-3 rounded-lg">
              <span class="text-sm font-semibold text-gray-500 block mb-2">Follow-up</span>
              <p class="text-base text-gray-700">{{ response.followupDetails }}</p>
            </div>
          </div>
        </div>

        <!-- Response Time Row -->
        <div class="grid grid-cols-3 gap-3">
          <div class="border-2 border-gray-200 p-3 rounded-lg">
            <span class="text-sm font-semibold text-gray-500 block mb-1">Response Time</span>
            <span :class="getResponseTimeColor(response.responseTime)" class="text-base font-semibold">
              {{ response.responseTime }}
            </span>
          </div>
          <div class="border-2 border-gray-200 p-3 rounded-lg">
            <span class="text-sm font-semibold text-gray-500 block mb-1">Remediation</span>
            <span class="text-base text-gray-700">{{ response.remediationDate }}</span>
          </div>
          <div class="border-2 border-gray-200 p-3 rounded-lg">
            <span class="text-sm font-semibold text-gray-500 block mb-1">Follow-up</span>
            <span class="text-base text-gray-700">{{ response.followupDate }}</span>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
defineProps({
  responses: Array,
  loading: Boolean
})

defineEmits(['go-back'])

const getResponseTimeColor = (time) => {
  if (!time) return 'text-gray-600'
  
  // Extract minutes from time string (e.g., "15 minutes" -> 15)
  const minutesMatch = time.match(/(\d+)\s*minutes?/i)
  if (!minutesMatch) return 'text-gray-600'
  
  const minutes = parseInt(minutesMatch[1])
  if (minutes <= 15) return 'text-green-600'
  if (minutes <= 30) return 'text-yellow-600'
  return 'text-red-600'
}
</script>
