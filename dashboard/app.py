import streamlit as st
import os
import sys
import os

# Add project root directory to Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
# Import project modules
from prediction.predict_disaster import predict_disaster
from routing.evacuation import run_evacuation
from maps.live_map import create_map
from alerts.alert_system import send_alert
from satellite.live_weather import get_weather


# -----------------------------
# Page Title
# -----------------------------
st.title("AI Disaster Monitoring & Rescue System")

st.write("AI-powered platform for disaster prediction, evacuation planning, and rescue monitoring.")

st.divider()


# -----------------------------
# Real-Time Weather Data
# -----------------------------
st.subheader("Real-Time Weather Data")

city = st.text_input("Enter City Name", "Chennai")

if st.button("Fetch Live Weather"):

    try:
        rain, temp, humidity, wind = get_weather(city)

        st.write("Rainfall:", rain)
        st.write("Temperature:", temp)
        st.write("Humidity:", humidity)
        st.write("Wind Speed:", wind)

        result = predict_disaster(rain, temp, humidity, wind)

        st.success(f"AI Prediction Result: {result}")

        if result == "HIGH DISASTER RISK":
            send_alert("⚠ Emergency: High Disaster Risk Detected")
            st.error("Emergency Alert Sent!")

    except:
        st.error("Weather API Error. Check your API key or internet connection.")

st.divider()


# -----------------------------
# Manual Disaster Prediction
# -----------------------------
st.subheader("Manual Disaster Risk Prediction")

rain = st.slider("Rainfall (mm)", 0, 500)
temp = st.slider("Temperature (°C)", 0, 50)
humidity = st.slider("Humidity (%)", 0, 100)
wind = st.slider("Wind Speed (km/h)", 0, 200)

if st.button("Predict Disaster Risk"):

    result = predict_disaster(rain, temp, humidity, wind)

    st.success(f"Prediction Result: {result}")

    if result == "HIGH DISASTER RISK":
        send_alert("⚠ Emergency: High Disaster Risk Detected")
        st.error("Emergency Alert Sent!")

st.divider()


# -----------------------------
# Evacuation Route Finder
# -----------------------------
st.subheader("Evacuation Route Finder")

st.write("Find the safest evacuation path to the nearest safe zone.")

if st.button("Find Safe Route"):

    route = run_evacuation()

    st.success("Safe Route Found")

    st.write("Evacuation Path:", " ➜ ".join(route))

st.divider()


# -----------------------------
# Disaster Map Generator
# -----------------------------
st.subheader("Generate Disaster Map")

st.write("Visualize disaster location on the map.")

if st.button("Show Disaster Map"):

    create_map(13.0827, 80.2707)

    st.success("Map Generated Successfully!")

    st.info("Open 'disaster_map.html' in your project folder to view the map.")

st.divider()


# -----------------------------
# Drone Human Detection
# -----------------------------
st.subheader("Drone Human Detection")

st.write("Start AI-powered drone camera to detect stranded people.")

if st.button("Start Drone Camera"):

    st.warning("Launching Drone Detection System...")

    os.system("python drone/yolo_drone_detection.py")

    st.success("Drone Camera Closed")
