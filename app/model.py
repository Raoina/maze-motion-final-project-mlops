import joblib

model = joblib.load("Random Forest_model.pkl")

def predict_hand_gesture(features: list) -> str:

    prediction = model.predict([features])
    return prediction[0]
