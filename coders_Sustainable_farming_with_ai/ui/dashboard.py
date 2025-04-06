import streamlit as st
import requests
import json
from utils.logger import log_info, log_error

# Set Streamlit page config
st.set_page_config(page_title="Sustainable Farming AI", page_icon="🌾", layout="wide")

# Title
st.title("🌾 Sustainable Farming AI Dashboard")
st.markdown("Welcome to the smart farming assistant. Get real-time recommendations for your crops, soil, and market insights!")

# Sidebar navigation
st.sidebar.header("Navigation")
user_type = st.sidebar.radio("I am a:", ("Farmer", "Advisor"))

# API endpoint
API_URL = "http://localhost:8000/farmer/request"

def send_farmer_request(payload):
    try:
        response = requests.post(API_URL, json=payload)
        response.raise_for_status()
        log_info(f"Farmer request successful ✅: {payload}")
        return response.json()
    except requests.RequestException as e:
        log_error(f"Farmer request failed ❌: {e}")
        return {"error": str(e)}

# Farmer form
if user_type == "Farmer":
    st.header("👨‍🌾 Farmer Input Form")
    with st.form("farmer_form"):
        crop = st.text_input("Crop Name", placeholder="e.g., Wheat")
        soil_type = st.text_input("Soil Type", placeholder="e.g., Loamy")
        region = st.text_input("Region", placeholder="e.g., Punjab")
        rainfall = st.number_input("Expected Rainfall (mm)", min_value=0)
        temperature = st.number_input("Expected Temperature (°C)", min_value=-10, max_value=60)
        submit = st.form_submit_button("Get Recommendations 🌱")

    if submit:
        payload = {
            "crop": crop,
            "soil_type": soil_type,
            "region": region,
            "rainfall": rainfall,
            "temperature": temperature
        }
        st.write("⏳ Processing your request...")
        response = send_farmer_request(payload)

        if "error" in response:
            st.error(f"Error: {response['error']}")
        else:
            st.success("✅ Recommendations Received!")
            st.json(response)

# Advisor section
elif user_type == "Advisor":
    st.header("🧑‍💼 Advisor Panel")
    st.markdown("This section is under development 🚧 Stay tuned!")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ for Sustainable Farming")
