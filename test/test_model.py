import pytest
import joblib
import pandas as pd

model = joblib.load("Random Forest_model.pkl")

test_input = pd.DataFrame([ [0]*63 ])

def test_model_prediction_shape():
    preds = model.predict(test_input)
   
    assert len(preds) == 1

def test_model_prediction_type():
    preds = model.predict(test_input)
    assert isinstance(preds[0], str)
