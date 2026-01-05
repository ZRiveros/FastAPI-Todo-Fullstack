# FastAPI Todo Backend

Backend API för Todo-applikationen byggd med FastAPI och MongoDB.

## Installation

```bash
# Skapa virtuell miljö
python3 -m venv .venv
source .venv/bin/activate

# Installera beroenden
pip install fastapi uvicorn motor pymongo
```

## Kör servern

```bash
uvicorn main:app --reload --port 8000
```

API:et kommer vara tillgängligt på `http://localhost:8000`

## Endpoints

- `GET /` - Välkomstmeddelande
- `GET /todos` - Hämta alla todos
- `GET /todos/{id}` - Hämta en specifik todo
- `POST /todos` - Skapa ny todo
- `PUT /todos/{id}` - Uppdatera todo
- `DELETE /todos/{id}` - Ta bort todo

## CORS

API:et är konfigurerat att acceptera requests från Angular frontend på port 4200.
