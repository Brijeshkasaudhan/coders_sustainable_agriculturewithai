from fastapi import APIRouter, Request
from agents.farmer_agent import process_farmer_input
from utils.logger import log_info, log_error

router = APIRouter()

@router.post("/farmer/request")
async def farmer_request(request: Request):
    try:
        data = await request.json()
        log_info(f"Received farmer request ✅: {data}")
        response = process_farmer_request(data)
        log_info(f"Response generated ✅: {response}")
        return response
    except Exception as e:
        log_error(f"Error processing farmer request ❌: {e}")
        return {"error": "Failed to process request"}
