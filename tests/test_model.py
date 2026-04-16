import joblib
from sklearn.metrics import r2_score
import numpy as np
import pandas as pd

def test_model_performance():
    model = joblib.load("stress_model.pkl")

    # Example test data (replace with real validation data)
    x_test = np.array([[55, 'Male', 'Teacher', 9.88, 37, 6.81, 4.08, 4, 11, 40, 10.0,
        395.20000000000005, 27.7848],
       [37, 'Female', 'Doctor', 9.42, 97, 4.48, 2.94, 3, 99, 197, 10.0,
        1855.74, 13.1712],
       [39, 'Female', 'Software Engineer', 1.07, 69, 6.38, 8.66, 3, 29,
        182, 1.0, 194.74, 55.2508]])
    y_test = np.array([10. , 10. ,  2.3])
    x_test=pd.DataFrame(x_test,columns=['age', 'gender', 'occupation', 'daily_screen_time_hours',
       'phone_usage_before_sleep_minutes', 'sleep_duration_hours',
       'sleep_quality_score', 'caffeine_intake_cups',
       'physical_activity_minutes', 'notifications_received_per_day',
       'mental_fatigue_score', 'screen_notification_interaction',
       'sleep_health_score'])

    y_pred = model.predict(x_test)

    acc = r2_score(y_test,y_pred)

    print("Model Accuracy:", acc)

    assert acc >= 0.80