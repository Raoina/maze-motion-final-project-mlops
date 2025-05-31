from fastapi import FastAPI
from app.model import predict_hand_gesture
from app.schemas import GestureRequest, GestureResponse

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Welcome to Hand Gesture API"}

@app.post("/predict", response_model=GestureResponse)
def predict_gesture(request: GestureRequest):
    gesture = predict_hand_gesture(request.features)
    return GestureResponse(gesture=gesture)
