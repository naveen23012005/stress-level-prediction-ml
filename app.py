import streamlit as st
import pandas as pd
import joblib

model = joblib.load("stress_model.pkl")

st.title("Stress Level Prediction App")

st.write("Enter lifestyle details to predict stress level")

age = st.number_input("Age",18,60)

gender = st.selectbox("Gender",["Male","Female","Other"])

occupation = st.selectbox(
"Occupation",
["Student","Engineer","Doctor","Teacher","Other"]
)

screen_time = st.number_input("Daily Screen Time (hours)",0.0,15.0)

phone_before_sleep = st.number_input(
"Phone Usage Before Sleep (minutes)",0,200
)

sleep_duration = st.number_input("Sleep Duration (hours)",0.0,12.0)

sleep_quality = st.slider("Sleep Quality Score",1,10)

caffeine = st.number_input("Caffeine Intake (cups)",0,10)

physical_activity = st.number_input(
"Physical Activity (minutes)",0,300
)

notifications = st.number_input(
"Notifications per day",0,500
)

mental_fatigue = st.slider("Mental Fatigue Score",1,10)

# create dataframe
input_data = pd.DataFrame({
"age":[age],
"gender":[gender],
"occupation":[occupation],
"daily_screen_time_hours":[screen_time],
"phone_usage_before_sleep_minutes":[phone_before_sleep],
"sleep_duration_hours":[sleep_duration],
"sleep_quality_score":[sleep_quality],
"caffeine_intake_cups":[caffeine],
"physical_activity_minutes":[physical_activity],
"notifications_received_per_day":[notifications],
"mental_fatigue_score":[mental_fatigue]
})

if st.button("Predict Stress Level"):

    prediction = model.predict(input_data)

    st.success(f"Predicted Stress Level: {prediction[0]:.2f}")