import os
import joblib
import numpy as np

# Get project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Correct model path
model_path = os.path.join(BASE_DIR, "models", "disaster_model.pkl")

# Load model
model = joblib.load(model_path)

def predict_disaster(rainfall, temperature, humidity, wind):
    data = np.array([[rainfall, temperature, humidity, wind]])
    prediction = model.predict(data)
    return prediction[0]
