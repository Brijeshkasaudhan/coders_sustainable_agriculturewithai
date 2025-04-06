from fastapi import FastAPI
from api import routes
from utils.logger import log_info, log_error

app = FastAPI()

try:
    app.include_router(routes.router)
    log_info("Routes included successfully ✅")
except Exception as e:
    log_error(f"Error including routes ❌: {e}")

@app.get("/")
async def root():
    log_info("Root endpoint accessed ✅")
    return {"message": "Welcome to Sustainable Farming AI API"}
