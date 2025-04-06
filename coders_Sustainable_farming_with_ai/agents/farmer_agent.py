from utils.logger import log_info, log_error

def process_farmer_input(farmer_data):
    try:
        log_info(f"Processing farmer input: {farmer_data}")
        # Process input data
        processed_data = {
            "name": farmer_data.get("name"),
            "location": farmer_data.get("location"),
            "soil_type": farmer_data.get("soil_type"),
            "crop_history": farmer_data.get("crop_history")
        }
        log_info(f"Processed farmer data: {processed_data}")
        return processed_data
    except Exception as e:
        log_error(f"Error processing farmer input: {e}")
        return None
