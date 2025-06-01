import joblib
from typing import List

model = joblib.load("Random Forest_model.pkl")

def predict_hand_gesture(features: List[float]) -> str:
    
    prediction = model.predict([features])
    return prediction[0]
