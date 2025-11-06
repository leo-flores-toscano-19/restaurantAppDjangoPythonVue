/**
 * API Service Layer
 * Handles all API calls to Django backend
 */

// Use relative URL when proxied through Vite, or absolute URL for direct access
const API_BASE_URL = '/api'

/**
 * Generic fetch function with error handling
 */
async function apiFetch(endpoint, options = {}) {
  try {
    const response = await fetch(`${API_BASE_URL}${endpoint}`, {
      headers: {
        'Content-Type': 'application/json',
        ...options.headers,
      },
      ...options,
    })

    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`)
    }

    return await response.json()
  } catch (error) {
    console.error(`API Error (${endpoint}):`, error)
    throw error
  }
}

// Sales API
export async function fetchSalesData() {
  return apiFetch('/sales/getStoreSales/')
}

export async function fetchSalesSorted(sortBy, sortDirection) {
  return apiFetch(`/sales/getStoreSalesSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Deliveries API
export async function fetchDeliveriesData() {
  return apiFetch('/deliveries/getStoreDeliveries/')
}

export async function fetchDeliveriesSorted(sortBy, sortDirection) {
  return apiFetch(`/deliveries/getStoreDeliveriesSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Critical Issues API
export async function fetchCriticalIssuesData() {
  return apiFetch('/criticalissues/getCriticalIssues/')
}

export async function fetchCriticalIssuesSorted(sortBy, sortDirection) {
  return apiFetch(`/criticalissues/getCriticalIssuesSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// POS Issues API
export async function fetchPosIssuesData() {
  return apiFetch('/posissues/getPosIssues/')
}

export async function fetchPosIssuesSorted(sortBy, sortDirection) {
  return apiFetch(`/posissues/getPosIssuesSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Promotions API
export async function fetchPromotionsData() {
  return apiFetch('/activepromotions/getPromotions/')
}

export async function fetchPromotionsSorted(sortBy, sortDirection) {
  return apiFetch(`/activepromotions/getPromotionsSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Performance API
export async function fetchPerformanceData() {
  return apiFetch('/performance/getStorePerformance/')
}

export async function fetchPerformanceSorted(sortBy, sortDirection) {
  return apiFetch(`/performance/getStorePerformanceSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Response Time API
export async function fetchResponseTimeData() {
  return apiFetch('/responsetime/getResponseTimes/')
}

export async function fetchResponseTimeSorted(sortBy, sortDirection) {
  return apiFetch(`/responsetime/getResponseTimesSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Weekly Events API
export async function fetchWeeklyEventsData() {
  return apiFetch('/weeklyevents/getWeeklyEvents/')
}

// Application Issue API (for chat)
export async function fetchApplicationIssue(question = '') {
  return apiFetch('/ApplicationIssue/getApplicationIssue/', {
    method: 'POST',
    body: JSON.stringify({
      agent: 'Application Issues',
      question: question,
      timestamp: Date.now()
    }),
  })
}

export async function fetchAllApplicationIssues() {
  return apiFetch('/ApplicationIssue/getAllApplicationIssues/')
}

// Ticket Status API
export async function fetchTicketStatus() {
  return apiFetch('/TicketStatus/getTicketStatus/', {
    method: 'POST',
    body: JSON.stringify({}),
  })
}

export async function fetchAllTicketStatus() {
  return apiFetch('/TicketStatus/getAllTicketStatus/')
}

// Feedback API
export async function fetchFeedbackData() {
  return apiFetch('/positiveFeedback/getPositiveFeedback/')
}

export async function fetchFeedbackSorted(sortBy, sortDirection) {
  return apiFetch(`/positiveFeedback/getPositiveFeedbackSorted/?sortBy=${sortBy}&sortDirection=${sortDirection}`)
}

// Configuration API
export async function fetchConfiguration() {
  return apiFetch('/Configuration/getConfiguration/', {
    method: 'POST',
    body: JSON.stringify({}),
  })
}

export async function fetchAllConfiguration() {
  return apiFetch('/Configuration/getAllConfiguration/')
}

// Calendar API
export async function fetchCalendarData() {
  return apiFetch('/calendar/getCalendarData/')
}

