from fastapi import FastAPI, Request
from prometheus_fastapi_instrumentator import Instrumentator
from prometheus_client import Counter, Histogram, Gauge
import time
from app.model import predict_hand_gesture
from app.schemas import GestureRequest, GestureResponse

app = FastAPI()

# Prometheus metrics
MODEL_ACCURACY = Gauge('model_accuracy', 'Accuracy of the model predictions') 
MISSING_VALUES_COUNT = Counter('missing_values_total', 'Total missing input values detected')
REQUEST_LATENCY = Histogram('request_latency_seconds', 'Latency of API requests in seconds') 
# auto expose /metrics endpoint
Instrumentator().instrument(app).expose(app)

def update_model_accuracy(new_accuracy):
    MODEL_ACCURACY.set(new_accuracy)

@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    REQUEST_LATENCY.observe(process_time)
    return response

@app.get("/")
def read_root():
    return {"message": "Welcome to Hand Gesture API"}

@app.post("/predict", response_model=GestureResponse)
async def predict(request: GestureRequest):
    missing_count = sum(1 for v in request.features if v is None)
    if missing_count > 0:
        MISSING_VALUES_COUNT.inc(missing_count)

    prediction = predict_hand_gesture(request.features)

    return GestureResponse(gesture=prediction)
