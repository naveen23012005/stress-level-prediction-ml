import joblib

model = joblib.load("models//stress_model.pkl")

def predict_stress(data):
    prediction = model.predict(data)
    return float(prediction[0])