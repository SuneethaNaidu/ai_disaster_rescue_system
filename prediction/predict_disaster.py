import joblib
import numpy as np
import os
import joblib
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "models", "disaster_model.pkl")

model = joblib.load(model_path)
model = joblib.load("models/disaster_model.pkl")

def predict_disaster(rainfall,temperature,humidity,wind):

    data = np.array([[rainfall,temperature,humidity,wind]])

    result = model.predict(data)

    if result == 1:
        return "HIGH DISASTER RISK"
    else:
        return "SAFE"
