# Getting Started med FastAPI Todo Backend

## Förutsättningar

- Python 3.8 eller högre
- MongoDB (lokal eller Atlas)

## Steg för steg

1. **Aktivera virtuell miljö**
   ```bash
   cd ~/fastapi_todo_front/fastapi-todo-backend
   python3 -m venv .venv
   source .venv/bin/activate
   ```

2. **Installera dependencies**
   ```bash
   pip install fastapi uvicorn motor pymongo
   ```

3. **Starta MongoDB** (om lokal)
   ```bash
   sudo systemctl start mongodb
   ```

4. **Kör servern**
   ```bash
   uvicorn main:app --reload --port 8000
   ```

5. **Testa API:et**
   Öppna `http://localhost:8000/docs` för Swagger dokumentation

## Miljövariabler (valfritt)

Skapa en `.env` fil:
```
MONGODB_URL=mongodb://localhost:27017
```

## Koppling med Frontend

Frontend (Angular) kör på port 4200 och är redan konfigurerad i CORS-inställningarna.
