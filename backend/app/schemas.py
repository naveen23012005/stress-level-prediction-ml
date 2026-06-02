from pydantic import BaseModel

class StressInput(BaseModel):
    age: int
    gender: str
    occupation: str
    daily_screen_time_hours: float
    phone_usage_before_sleep_minutes: int
    sleep_duration_hours: float
    sleep_quality_score: int
    caffeine_intake_cups: int
    physical_activity_minutes: int
    notifications_received_per_day: int
    mental_fatigue_score: int