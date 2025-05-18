from fastapi import FastAPI
from database import engine
from models.base import Base
from auth_routes import router as auth_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Create tables if they don't exist
Base.metadata.create_all(bind=engine)

# Register routes from other files
app.include_router(auth_router)

@app.get("/")
def root():
    return {"message": "Hello from FastAPI"}
