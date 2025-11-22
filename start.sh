#!/bin/bash

# Restaurant App Start Script
# Starts both backend (Django) and frontend (Vue.js) servers
# Opens the application in the default browser

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
BACKEND_DIR="$SCRIPT_DIR/backend"
FRONTEND_DIR="$SCRIPT_DIR/frontend"
PID_FILE="$SCRIPT_DIR/.app_pids"

# Function to cleanup on exit
cleanup() {
    echo -e "\n${YELLOW}Cleaning up...${NC}"
    if [ -f "$PID_FILE" ]; then
        while read pid; do
            if ps -p $pid > /dev/null 2>&1; then
                kill $pid 2>/dev/null || true
            fi
        done < "$PID_FILE"
        rm -f "$PID_FILE"
    fi
    exit 0
}

# Trap Ctrl+C
trap cleanup SIGINT SIGTERM

# Check if servers are already running
check_port() {
    local port=$1
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        return 0
    else
        return 1
    fi
}

# Check backend port (8000)
if check_port 8000; then
    echo -e "${YELLOW}Backend server is already running on port 8000${NC}"
    read -p "Do you want to stop it and restart? (y/n) " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        lsof -ti:8000 | xargs kill -9 2>/dev/null || true
        sleep 1
    else
        echo "Exiting..."
        exit 1
    fi
fi

# Check frontend port (5173 or 5174)
FRONTEND_PORT=5173
if check_port 5173; then
    FRONTEND_PORT=5174
    if check_port 5174; then
        echo -e "${RED}Both ports 5173 and 5174 are in use. Please free one up.${NC}"
        exit 1
    fi
fi

# Initialize PID file
> "$PID_FILE"

echo -e "${GREEN}Starting Restaurant App...${NC}\n"

# Start Backend Server
echo -e "${YELLOW}Starting Django backend server...${NC}"
cd "$BACKEND_DIR"

# Check if virtual environment exists
if [ ! -d "venv" ]; then
    echo -e "${RED}Virtual environment not found. Please run: python3 -m venv venv${NC}"
    exit 1
fi

# Activate virtual environment and start server
source venv/bin/activate
python manage.py runserver > /tmp/django_server.log 2>&1 &
BACKEND_PID=$!
echo $BACKEND_PID >> "$PID_FILE"
echo -e "${GREEN}Backend server started (PID: $BACKEND_PID) on http://localhost:8000${NC}"

# Wait for backend to be ready
echo -e "${YELLOW}Waiting for backend server to be ready...${NC}"
for i in {1..30}; do
    if curl -s http://localhost:8000 > /dev/null 2>&1; then
        echo -e "${GREEN}Backend server is ready!${NC}"
        break
    fi
    sleep 1
    if [ $i -eq 30 ]; then
        echo -e "${RED}Backend server failed to start. Check /tmp/django_server.log${NC}"
        cleanup
        exit 1
    fi
    echo -n "."
done
echo ""

# Start Frontend Server
echo -e "${YELLOW}Starting Vue.js frontend server...${NC}"
cd "$FRONTEND_DIR"

# Check if node_modules exists
if [ ! -d "node_modules" ]; then
    echo -e "${YELLOW}node_modules not found. Installing dependencies...${NC}"
    npm install
fi

# Start frontend dev server
npm run dev > /tmp/vite_server.log 2>&1 &
FRONTEND_PID=$!
echo $FRONTEND_PID >> "$PID_FILE"

# Wait a moment for Vite to start and determine the actual port
sleep 3

# Try to get the actual port from the log or use default
ACTUAL_PORT=$FRONTEND_PORT
if grep -q "Local:" /tmp/vite_server.log 2>/dev/null; then
    ACTUAL_PORT=$(grep "Local:" /tmp/vite_server.log | grep -oE ":[0-9]+" | head -1 | tr -d ':')
fi

echo -e "${GREEN}Frontend server started (PID: $FRONTEND_PID) on http://localhost:$ACTUAL_PORT${NC}"

# Wait for frontend to be ready
echo -e "${YELLOW}Waiting for frontend server to be ready...${NC}"
for i in {1..30}; do
    if curl -s http://localhost:$ACTUAL_PORT > /dev/null 2>&1; then
        echo -e "${GREEN}Frontend server is ready!${NC}"
        break
    fi
    sleep 1
    if [ $i -eq 30 ]; then
        echo -e "${RED}Frontend server failed to start. Check /tmp/vite_server.log${NC}"
        cleanup
        exit 1
    fi
    echo -n "."
done
echo ""

# Open browser
echo -e "${YELLOW}Opening browser...${NC}"
sleep 2

# Detect OS and open browser accordingly
if [[ "$OSTYPE" == "darwin"* ]]; then
    # macOS
    open "http://localhost:$ACTUAL_PORT"
elif [[ "$OSTYPE" == "linux-gnu"* ]]; then
    # Linux
    if command -v xdg-open &> /dev/null; then
        xdg-open "http://localhost:$ACTUAL_PORT"
    elif command -v google-chrome &> /dev/null; then
        google-chrome "http://localhost:$ACTUAL_PORT" &
    elif command -v chromium-browser &> /dev/null; then
        chromium-browser "http://localhost:$ACTUAL_PORT" &
    else
        echo -e "${YELLOW}Please open http://localhost:$ACTUAL_PORT in your browser${NC}"
    fi
elif [[ "$OSTYPE" == "msys" || "$OSTYPE" == "cygwin" ]]; then
    # Windows (Git Bash)
    start "http://localhost:$ACTUAL_PORT"
else
    echo -e "${YELLOW}Please open http://localhost:$ACTUAL_PORT in your browser${NC}"
fi

echo -e "\n${GREEN}========================================${NC}"
echo -e "${GREEN}Application is running!${NC}"
echo -e "${GREEN}Backend:  http://localhost:8000${NC}"
echo -e "${GREEN}Frontend: http://localhost:$ACTUAL_PORT${NC}"
echo -e "${GREEN}========================================${NC}"
echo -e "\n${YELLOW}Press Ctrl+C to stop the servers${NC}\n"

# Keep script running and show logs
tail -f /tmp/django_server.log /tmp/vite_server.log 2>/dev/null || {
    # If tail fails, just wait
    while true; do
        sleep 1
        # Check if processes are still running
        if ! ps -p $BACKEND_PID > /dev/null 2>&1; then
            echo -e "${RED}Backend server stopped unexpectedly${NC}"
            cleanup
            exit 1
        fi
        if ! ps -p $FRONTEND_PID > /dev/null 2>&1; then
            echo -e "${RED}Frontend server stopped unexpectedly${NC}"
            cleanup
            exit 1
        fi
    done
}

