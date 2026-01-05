from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from routes.todo import router as todo_router


app = FastAPI(
    title="Todo API",
    description="A simple Todo API built with FastAPI and MongoDB",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
   allow_origins=[
    "http://localhost:4200",
    "http://127.0.0.1:4200",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
   ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo_router)


@app.get("/")
def root():
    return {"message": "Welcome to the Todo API"}