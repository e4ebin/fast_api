import numpy as np
import joblib

model=joblib.load('model.pkl')

def predict_hd(age,sex,chest_pain,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal):
    try:
        _input=np.array([[age,sex,chest_pain,trestbps,chol,fbs,restecg,thalach,exang,oldpeak,slope,ca,thal]])
        _prediction=model.predict(_input)
        return _prediction
    except Exception as e:
        raise Exception(e)
