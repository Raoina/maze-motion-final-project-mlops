# ML Course Final Project - Gesture Control Game

## Introduction

This project implements a gesture-controlled maze game using machine learning for hand gesture recognition. Players control the game using hand gestures captured through their webcam, which are classified into navigation commands.

The project consists of two parts:
- Frontend game interface (HTML, JS)
- Backend ML model training, evaluation, and API deployment for gesture recognition.

---

## 🚀 Quick Start (Frontend)

1. Install the Live Server extension in VS Code:
   - Open VS Code
   - Go to Extensions (Ctrl+Shift+X)
   - Search for "Live Server"
   - Install the extension by Ritwick Dey

2. Launch the project:
   - Right-click on `index.html`
   - Select "Open with Live Server"
   - The game should open in your default browser at `http://localhost:5500`

---

## 📁 Project Structure

- `index.html` - Main game interface  
- `api-call.js` - ML model API integration (calls backend model)  
- `cam.js` - Webcam handling and gesture processing  
- `keyboard.js` - Keyboard controls implementation (fallback)  
- `maze.js` - Maze game logic  
- `mp.js` - Media processing utilities  

---

## 🔧 Important Implementation Note

In `api-call.js`, there is a TODO section to implement:

```javascript
// TODO: Call your model's API here
// and return the predicted label
// Possible labels: "up", "down", "left", "right", null
// null means stop & wait for the next gesture
```
## Important Implementation Note

You need to replace the current placeholder with your actual ML model API call. The function should:

- Take the processed tensor (`processed_t`) as input  
- Call your deployed ML model's API endpoint  
- Return one of: `"up"`, `"down"`, `"left"`, `"right"`, or `null`  

---

## Backend: ML Model Training and Evaluation

### Dataset

The dataset contains normalized hand landmark points labeled with four gestures:

- `"one"`  
- `"two_up"`  
- `"three"`  
- `"four"`  

### Preprocessing

Each landmark point is normalized relative to the wrist and scaled by the distance between wrist and middle finger landmarks.

### Models Trained

- Random Forest  
- Support Vector Machine (SVM)  
- K-Nearest Neighbors (KNN)  

### Evaluation Results Summary

| Model         | Accuracy | Precision | Recall | F1-Score |
|---------------|----------|-----------|--------|----------|
| Random Forest | 0.98     | 0.98      | 0.98   | 0.98     |
| SVM           | 0.29     | 0.56      | 0.29   | 0.14     |
| KNN           | 0.97     | 0.97      | 0.97   | 0.97     |

### Confusion Matrices

**Random Forest:**

[[321   0   5   1]
 [  0 251   0   2]
 [ 10   0 281   0]
 [  0   0   1 268]]


**SVM:**

[[322   0   5   0]
 [249   4   0   0]
 [286   0   5   0]
 [264   3   1   1]]


**KNN:**

[[324   0   2   1]
 [  7 248   3   0]
 [ 15   0 276   0]
 [  2   6   1 260]]

---

### Model Selection

The **Random Forest** model was selected for deployment due to its superior accuracy and balanced performance.

---

## Next Steps

- Deploy the Random Forest model as a REST API backend for real-time gesture recognition.  
- Integrate the backend API with the frontend game for gesture-based controls.  
- Optionally extend the model with more gestures (e.g., directional hand signs).  

---

## How to Run

### Frontend

- Follow the Quick Start instructions above to run the game in your browser.
----
