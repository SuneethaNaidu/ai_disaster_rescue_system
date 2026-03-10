import joblib
import numpy as np

model = joblib.load("models/disaster_model.pkl")

def predict_disaster(rainfall,temperature,humidity,wind):

    data = np.array([[rainfall,temperature,humidity,wind]])

    result = model.predict(data)

    if result == 1:
        return "HIGH DISASTER RISK"
    else:
        return "SAFE"
