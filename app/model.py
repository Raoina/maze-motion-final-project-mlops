import joblib
from typing import List
import os

model_path = os.path.join(os.path.dirname(__file__), "..", "Random Forest_model.pkl")
model = joblib.load(model_path)

def predict_hand_gesture(features: List[float]) -> str:
    prediction = model.predict([features])
    return prediction[0]
