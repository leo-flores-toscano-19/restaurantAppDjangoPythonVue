<template>
  <div class="h-full flex flex-col">
    <div class="flex justify-between items-center mb-4">
      <h2 class="text-2xl font-bold">Store Performance Report</h2>
      <p class="text-sm text-gray-600">Click on column headers to sort</p>
    </div>
    <div v-if="loading" class="flex items-center justify-center h-full">
      <div class="animate-spin rounded-full h-12 w-12 border-b-2 border-blue-500"></div>
    </div>
    <div v-else class="flex-1 overflow-y-auto">
      <div class="shadow overflow-hidden border-b border-gray-200 sm:rounded-lg">
        <table class="min-w-full divide-y divide-gray-200">
          <thead class="bg-gray-50">
            <tr>
              <th 
                scope="col" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                @click="sort('storeName')"
              >
                Store Name
                <span v-if="sortBy === 'storeName'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                scope="col" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                @click="sort('location')"
              >
                Location
                <span v-if="sortBy === 'location'" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
              <th 
                v-for="month in months" 
                :key="month"
                scope="col" 
                class="px-6 py-3 text-left text-xs font-medium text-gray-500 uppercase tracking-wider cursor-pointer hover:bg-gray-100"
                @click="sort(`performance.${month}`)"
              >
                {{ month }}
                <span v-if="sortBy === `performance.${month}`" class="ml-1">{{ sortDirection === 'asc' ? '↑' : '↓' }}</span>
              </th>
            </tr>
          </thead>
          <tbody class="bg-white divide-y divide-gray-200">
            <tr v-for="store in stores" :key="store.storeName" class="hover:bg-gray-50">
              <td class="px-6 py-4 whitespace-nowrap text-sm font-medium text-gray-900">{{ store.storeName }}</td>
              <td class="px-6 py-4 whitespace-nowrap text-sm text-gray-500">{{ store.location }}</td>
              <td 
                v-for="month in months" 
                :key="month"
                class="px-6 py-4 whitespace-nowrap text-sm text-gray-500"
              >
                {{ formatNumber(store.performance.find(p => p.month === month)?.sales || 0) }}
              </td>
            </tr>
          </tbody>
        </table>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'

const props = defineProps({
  stores: Array,
  loading: Boolean
})

const emit = defineEmits(['go-back', 'sort'])

const sortBy = ref('storeName')
const sortDirection = ref('asc')

const months = computed(() => {
  if (!props.stores || props.stores.length === 0) return []
  return props.stores[0].performance?.map(p => p.month) || []
})

const formatNumber = (value) => {
  return new Intl.NumberFormat('en-US').format(value)
}

const sort = (column) => {
  if (sortBy.value === column) {
    sortDirection.value = sortDirection.value === 'asc' ? 'desc' : 'asc'
  } else {
    sortBy.value = column
    sortDirection.value = 'asc'
  }
  
  emit('sort', { column, direction: sortDirection.value })
}
</script>
