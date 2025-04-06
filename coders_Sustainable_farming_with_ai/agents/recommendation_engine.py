from utils.logger import log_info, log_error

def generate_recommendation(advice, market_data):
    try:
        log_info("Generating final recommendation ✅")
        recommendation = f"{advice} Consider selling {market_data['crop_name']} at ₹{market_data['price']} per unit."
        log_info(f"Final recommendation: {recommendation}")
        return recommendation
    except Exception as e:
        log_error(f"Error generating recommendation: {e}")
        return "Error in generating recommendation."
