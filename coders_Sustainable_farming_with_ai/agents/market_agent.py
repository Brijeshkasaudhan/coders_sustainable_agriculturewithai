from utils.logger import log_info, log_error

def analyze_market(crop_name):
    try:
        log_info(f"Analyzing market trends for crop: {crop_name}")
        # Dummy market data
        market_data = {
            "crop_name": crop_name,
            "price": 25.0,
            "demand": 85
        }
        log_info(f"Market data: {market_data}")
        return market_data
    except Exception as e:
        log_error(f"Error analyzing market data: {e}")
        return None
