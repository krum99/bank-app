from fastapi import FastAPI
from database import engine
from models.base import Base
from auth_routes import router as auth_router

app = FastAPI()

# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Register routes from other files
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}
