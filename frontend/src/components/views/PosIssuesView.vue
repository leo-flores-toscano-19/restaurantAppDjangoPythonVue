<template>
  <div class="h-full flex flex-col">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-xl font-semibold text-gray-800">POS Issues Report</h2>
      <button @click="loadIssues()" class="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">
        Refresh Data
      </button>
    </div>
    <div v-if="loading" class="flex items-center justify-center h-full">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>
    <div v-else class="flex-1 overflow-auto">
      <div class="overflow-x-auto">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th 
                @click="sortIssues('orderId')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Order ID
                <span v-if="sortBy === 'orderId'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('posId')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                POS ID
                <span v-if="sortBy === 'posId'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('monkeyTax')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Monkey Tax
                <span v-if="sortBy === 'monkeyTax'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('posTax')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                POS Tax
                <span v-if="sortBy === 'posTax'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('monkeyTotal')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Monkey Total
                <span v-if="sortBy === 'monkeyTotal'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('posTotal')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                POS Total
                <span v-if="sortBy === 'posTotal'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('postedOn')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Posted On
                <span v-if="sortBy === 'postedOn'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('logDetail')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Log Detail
                <span v-if="sortBy === 'logDetail'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('date')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Date
                <span v-if="sortBy === 'date'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                @click="sortIssues('time')" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
              >
                Time
                <span v-if="sortBy === 'time'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="issue in posIssues" :key="issue.orderId" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ issue.orderId }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ issue.posId }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ formatCurrency(issue.monkeyTax) }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ formatCurrency(issue.posTax) }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ formatCurrency(issue.monkeyTotal) }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ formatCurrency(issue.posTotal) }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ issue.postedOn }}</td>
              <td 
                class="px-6 py-4 whitespace-nowrap text-sm"
                :class="issue.logDetail.includes('mismatch') ? 'text-red-600' : 'text-green-600'"
              >
                {{ issue.logDetail }}
              </td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ issue.date }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-900">{{ issue.time }}</td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'

const props = defineProps({
  posIssues: Array,
  loading: Boolean
})

const emit = defineEmits(['go-back', 'sort'])

const sortBy = ref('orderId')
const sortDirection = ref('asc')

const formatCurrency = (value) => {
  return new Intl.NumberFormat('en-US', {
    style: 'currency',
    currency: 'USD'
  }).format(value)
}

const loadIssues = async () => {
  emit('sort', { action: 'reload' })
}

const sortIssues = (column) => {
  if (sortBy.value === column) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = column
    sortDirection.value = 'asc'
  }
  
  emit('sort', { column, direction: sortDirection.value })
}
</script>
