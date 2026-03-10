import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib

data = pd.read_csv("data/disaster_data.csv")

X = data[['rainfall','temperature','humidity','wind_speed']]
y = data['disaster']

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)

model = RandomForestClassifier()

model.fit(X_train,y_train)

joblib.dump(model,"models/disaster_model.pkl")

print("Model Trained and Saved")
