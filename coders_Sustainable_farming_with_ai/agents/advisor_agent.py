from utils.logger import log_info, log_error

def generate_advice(farmer_data, weather_data, market_data):
    try:
        log_info("Generating advice for the farmer ✅")
        # Simple logic for advice generation
        if weather_data['rainfall'] < 50:
            advice = "Consider drought-resistant crops."
        elif market_data['demand'] > 80:
            advice = "High demand crops are recommended."
        else:
            advice = "Maintain soil health with cover crops."

        log_info(f"Generated advice: {advice}")
        return advice
    except Exception as e:
        log_error(f"Error generating advice: {e}")
        return "Error in generating advice."
