import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import mlflow
import mlflow.sklearn
import matplotlib.pyplot as plt
import os
import joblib
import numpy as np

mlflow.set_experiment("hand_gesture_classification")

df = pd.read_csv('hand_landmarks_data.csv')
filtered_df = df[df['label'].isin(["one", "two_up", "three", "four"])]

def preprocess_landmarks(row):
    wrist_x, wrist_y = row[0], row[1]
    mid_finger_x, mid_finger_y = row[36], row[37]
    processed = []
    for i in range(0, 63, 3):
        x = row[i] - wrist_x
        y = row[i+1] - wrist_y
        x /= (mid_finger_x - wrist_x) if (mid_finger_x - wrist_x) != 0 else 1
        y /= (mid_finger_y - wrist_y) if (mid_finger_y - wrist_y) != 0 else 1
        z = row[i+2]
        processed.extend([x, y, z])
    return processed

features = filtered_df.drop('label', axis=1)
labels = filtered_df['label']
processed_features = features.apply(preprocess_landmarks, axis=1, result_type='expand')

X_train, X_test, y_train, y_test = train_test_split(
    processed_features, labels, test_size=0.2, random_state=42, stratify=labels
)

models = {
    'Random Forest': RandomForestClassifier(),
    'SVM': SVC(probability=True),
    'KNN': KNeighborsClassifier()
}

metrics_summary = {}

for name, model in models.items():
    with mlflow.start_run(run_name=name):
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)

        acc = accuracy_score(y_test, y_pred)
        precision = precision_score(y_test, y_pred, average='weighted', zero_division=0)
        recall = recall_score(y_test, y_pred, average='weighted', zero_division=0)
        f1 = f1_score(y_test, y_pred, average='weighted', zero_division=0)

        mlflow.log_metric("accuracy", acc)
        mlflow.log_metric("precision", precision)
        mlflow.log_metric("recall", recall)
        mlflow.log_metric("f1_score", f1)

        mlflow.sklearn.log_model(model, f"{name}_model", input_example=X_train.head(1))

        joblib.dump(model, f"{name}_model.pkl")
        print(f"Saved {name} model locally as {name}_model.pkl")

        dummy_input = np.random.rand(63).reshape(1, -1)
        dummy_pred = model.predict(dummy_input)
        print(f"Dummy input prediction for {name}: {dummy_pred}")

        metrics_summary[name] = {
            "Accuracy": acc,
            "Precision": precision,
            "Recall": recall,
            "F1 Score": f1
        }

        plt.figure(figsize=(8, 5))
        bars = plt.bar(metrics_summary[name].keys(), metrics_summary[name].values(),
                       color=['skyblue', 'orange', 'green', 'red'])
        plt.ylim(0, 1)
        plt.title(f"Metrics for {name}")
        plt.xlabel("Metric")
        plt.ylabel("Score")
        for bar in bars:
            yval = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2, yval + 0.01,
                     f'{yval:.2f}', ha='center', va='bottom')

        plot_path = f"{name}_metrics_plot.png"
        plt.savefig(plot_path)
        mlflow.log_artifact(plot_path)
        plt.close()
        os.remove(plot_path)

print("All models trained, evaluated, charted, logged, and saved locally successfully.")
