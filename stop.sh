#!/bin/bash

# Restaurant App Stop Script
# Stops both backend (Django) and frontend (Vue.js) servers

set -e

# Colors for output
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Get the directory where the script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
PID_FILE="$SCRIPT_DIR/.app_pids"

echo -e "${YELLOW}Stopping Restaurant App...${NC}\n"

# Function to kill process by PID
kill_process() {
    local pid=$1
    local name=$2
    if ps -p $pid > /dev/null 2>&1; then
        kill $pid 2>/dev/null || true
        sleep 1
        # Force kill if still running
        if ps -p $pid > /dev/null 2>&1; then
            kill -9 $pid 2>/dev/null || true
        fi
        echo -e "${GREEN}Stopped $name (PID: $pid)${NC}"
        return 0
    else
        echo -e "${YELLOW}$name (PID: $pid) was not running${NC}"
        return 1
    fi
}

# Kill processes from PID file
if [ -f "$PID_FILE" ]; then
    while read pid; do
        if [ ! -z "$pid" ]; then
            kill_process $pid "Process"
        fi
    done < "$PID_FILE"
    rm -f "$PID_FILE"
    echo ""
fi

# Also kill by port (in case PID file is missing)
# Kill Django server on port 8000
if lsof -Pi :8000 -sTCP:LISTEN -t >/dev/null 2>&1 ; then
    echo -e "${YELLOW}Killing process on port 8000 (Django backend)...${NC}"
    lsof -ti:8000 | xargs kill -9 2>/dev/null || true
    echo -e "${GREEN}Stopped Django backend server${NC}"
fi

# Kill Vite server on ports 5173 and 5174
for port in 5173 5174; do
    if lsof -Pi :$port -sTCP:LISTEN -t >/dev/null 2>&1 ; then
        echo -e "${YELLOW}Killing process on port $port (Vite frontend)...${NC}"
        lsof -ti:$port | xargs kill -9 2>/dev/null || true
        echo -e "${GREEN}Stopped Vite frontend server on port $port${NC}"
    fi
done

echo -e "\n${GREEN}All servers stopped!${NC}"

