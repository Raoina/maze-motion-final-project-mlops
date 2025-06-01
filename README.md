# Hand Gesture Recognition API

This repository contains the production-ready API for hand gesture recognition using a Random Forest model. The API is built with FastAPI and includes monitoring metrics exposed via Prometheus and visualized using Grafana.

---

## Monitoring Metrics Explanation

To ensure the system's reliability and performance, we monitor three key metrics related to the model, data, and server:

### 1. Model-related Metric: `MODEL_ACCURACY`
- **Description:**  
  This metric tracks the accuracy of the model's predictions. Accuracy is the proportion of correct predictions made by the model out of all predictions. Monitoring accuracy is crucial to ensure that the model maintains high prediction quality over time.
- **Reasoning:**  
  A sudden drop in accuracy can indicate model degradation or changes in input data distribution, signaling the need for retraining or investigation.  
- **Metric Type:** Gauge  
- **Source:**  
  [Scikit-learn accuracy_score](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.accuracy_score.html)

---

### 2. Data-related Metric: `MISSING_VALUES_COUNT`
- **Description:**  
  This counter tracks the total number of missing values detected in the input features of prediction requests.
- **Reasoning:**  
  Missing input values can adversely affect prediction accuracy and model behavior. Monitoring the count of missing values helps detect data quality issues early, prompting necessary data validation or preprocessing improvements.  
- **Metric Type:** Counter  
- **Source:**  
  [Handling Missing Data in Machine Learning](https://machinelearningmastery.com/handle-missing-data-python/)

---

### 3. Server-related Metric: `REQUEST_LATENCY`
- **Description:**  
  This histogram measures the latency (response time) of API requests in seconds.
- **Reasoning:**  
  Request latency is a critical factor affecting user experience. High latency may indicate server performance issues or resource bottlenecks. Tracking latency distribution helps maintain responsive and scalable API service.  
- **Metric Type:** Histogram  
- **Source:**  
  [Prometheus Histogram Best Practices](https://prometheus.io/docs/practices/histograms/)

---

## System Monitoring Setup

The metrics are exposed via the `/metrics` endpoint, integrated using the `prometheus_fastapi_instrumentator` library. Visualization is done using Grafana dashboards, which connect to Prometheus to show real-time monitoring data.

## How to Run

- Start the FastAPI app with Docker Compose to include Prometheus and Grafana services.
- Access the API documentation at: `http://localhost:8010/docs`
- Access Prometheus metrics at: `http://localhost:8010/metrics`
- Access Grafana dashboard at the configured port (usually `http://localhost:3000`)

---
