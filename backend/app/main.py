from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import pandas as pd

from app.schemas import StressInput
from app.model_loader import predict_stress
from app.db import get_connection

app = FastAPI(title="Stress Level Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_stress_category(score: float):
    if score <= 2:
        return "Very Low Stress"
    elif score <= 4:
        return "Low Stress"
    elif score <= 6:
        return "Moderate Stress"
    elif score <= 8:
        return "High Stress"
    else:
        return "Very High Stress"


@app.get("/")
def home():
    return {"message": "Stress Level Prediction API is running"}


@app.get("/health")
def health():
    return {"status": "healthy"}


from fastapi import HTTPException

@app.post("/predict")
def predict(data: StressInput):
    try:
        input_df = pd.DataFrame({
            "age": [data.age],
            "gender": [data.gender],
            "occupation": [data.occupation],
            "daily_screen_time_hours": [data.daily_screen_time_hours],
            "phone_usage_before_sleep_minutes": [data.phone_usage_before_sleep_minutes],
            "sleep_duration_hours": [data.sleep_duration_hours],
            "sleep_quality_score": [data.sleep_quality_score],
            "caffeine_intake_cups": [data.caffeine_intake_cups],
            "physical_activity_minutes": [data.physical_activity_minutes],
            "notifications_received_per_day": [data.notifications_received_per_day],
            "mental_fatigue_score": [data.mental_fatigue_score]
        })

        stress_score = predict_stress(input_df)
        stress_category = get_stress_category(stress_score)

        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            INSERT INTO stress_predictions (
                age,
                gender,
                occupation,
                daily_screen_time_hours,
                phone_usage_before_sleep_minutes,
                sleep_duration_hours,
                sleep_quality_score,
                caffeine_intake_cups,
                physical_activity_minutes,
                notifications_received_per_day,
                mental_fatigue_score,
                stress_score,
                stress_category
            )
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (
            data.age,
            data.gender,
            data.occupation,
            data.daily_screen_time_hours,
            data.phone_usage_before_sleep_minutes,
            data.sleep_duration_hours,
            data.sleep_quality_score,
            data.caffeine_intake_cups,
            data.physical_activity_minutes,
            data.notifications_received_per_day,
            data.mental_fatigue_score,
            stress_score,
            stress_category
        ))

        connection.commit()
        cursor.close()
        connection.close()

        return {
            "stress_score": round(stress_score, 2),
            "stress_category": stress_category,
            "message": "Prediction saved successfully"
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))