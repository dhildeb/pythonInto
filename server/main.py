from fastapi import FastAPI
from server.api.v1 import cards
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include the routers
app.include_router(cards.router, prefix="/api/v1/cards", tags=["cards"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}