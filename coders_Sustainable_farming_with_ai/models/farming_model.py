from utils.logger import log_info, log_error

class FarmingModel:
    def __init__(self):
        try:
            log_info("Initializing Farming Model ✅")
            self.model_data = {
                "Wheat": {"soil": "Loamy", "rainfall": (120, 200)},
                "Rice": {"soil": "Clayey", "rainfall": (150, 300)},
                "Maize": {"soil": "Sandy", "rainfall": (100, 150)},
            }
            log_info(f"Model data loaded: {self.model_data} ✅")
        except Exception as e:
            log_error(f"Error initializing Farming Model ❌: {e}")

    def predict(self, farmer_data, weather_data):
        try:
            log_info("Predicting suitable crops ✅")
            suitable_crops = []
            for crop, requirements in self.model_data.items():
                if (farmer_data.get("soil_type") == requirements["soil"] and
                        requirements["rainfall"][0] <= weather_data.get("rainfall", 0) <= requirements["rainfall"][1]):
                    suitable_crops.append(crop)

            log_info(f"Suitable crops: {suitable_crops} ✅")
            return suitable_crops
        except Exception as e:
            log_error(f"Error in prediction ❌: {e}")
            return []
