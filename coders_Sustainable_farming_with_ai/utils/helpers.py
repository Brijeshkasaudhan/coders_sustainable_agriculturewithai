# utils/helpers.py

import pandas as pd
from utils.logger import log_info

def load_farmer_advisor_data():
    try:
        data = pd.read_csv('data/farmer_advisor_dataset.csv')
        log_info("Farmer-Advisor dataset loaded successfully ✅")
        return data
    except Exception as e:
        log_info(f"Error loading Farmer-Advisor dataset: {e}")
        return None

def load_market_researcher_data():
    try:
        data = pd.read_csv('data/market_researcher_dataset.csv')
        log_info("Market Researcher dataset loaded successfully ✅")
        return data
    except Exception as e:
        log_info(f"Error loading Market Researcher dataset: {e}")
        return None
