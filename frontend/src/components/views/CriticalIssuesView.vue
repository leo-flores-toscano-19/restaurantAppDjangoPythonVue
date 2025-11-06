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
    <div v-if="loading" class="flex items-center justify-center h-full">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>
    <div v-else class="flex-1 overflow-auto">
      <h2 class="text-2xl font-bold mb-4">Critical Issues</h2>
      <table class="min-w-full divide-y divide-gray-200">
        <thead class="bg-gray-50">
          <tr>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Store</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Module</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Issue</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Rating</th>
            <th class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase">Impact</th>
          </tr>
        </thead>
        <tbody class="bg-white divide-y divide-gray-200">
          <tr v-for="issue in issues" :key="issue.id" class="hover:bg-gray-50">
            <td class="px-6 py-4 whitespace-nowrap text-sm font-medium">{{ issue.storeName }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">{{ issue.module }}</td>
            <td class="px-6 py-4 text-sm">{{ issue.complaint }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">{{ issue.rating }}</td>
            <td class="px-6 py-4 whitespace-nowrap text-sm">{{ issue.impact }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script setup>
defineProps({
  issues: Array,
  loading: Boolean
})
defineEmits(['go-back'])
</script>

