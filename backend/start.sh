#!/bin/bash

# Starta MongoDB om den inte redan körs
if ! pgrep -x "mongod" > /dev/null; then
    echo "Startar MongoDB..."
    sudo -u mongodb mongod --dbpath /var/lib/mongodb --logpath /var/log/mongodb/mongod.log --fork
    sleep 2
else
    echo "MongoDB kör redan"
fi

# Aktivera virtual environment och starta FastAPI
echo "Startar FastAPI backend..."
cd "$(dirname "$0")"
source .venv/bin/activate
uvicorn main:app --reload --port 8000
