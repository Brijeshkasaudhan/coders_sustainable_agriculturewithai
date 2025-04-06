from utils.logger import log_info, log_error

def fetch_weather_data(location):
    try:
        log_info(f"Fetching weather data for location: {location}")
        # Dummy data for now
        weather_data = {
            "location": location,
            "temperature": 28,
            "rainfall": 45,
            "humidity": 60
        }
        log_info(f"Weather data: {weather_data}")
        return weather_data
    except Exception as e:
        log_error(f"Error fetching weather data: {e}")
        return None
