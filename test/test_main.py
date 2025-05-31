from fastapi.testclient import TestClient
from app.main import app  # تأكد إن ملف main.py موجود في فولدر app وفيه متغير app

client = TestClient(app)

def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Welcome to Hand Gesture API"}

def test_predict_gesture():
    features_input = [0.0] * 63  
    response = client.post("/predict", json={"features": features_input})
    assert response.status_code == 200
    data = response.json()
    assert "gesture" in data
    assert isinstance(data["gesture"], str)
