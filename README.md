# 📱 Stress Level Prediction Using Machine Learning

## 📌 Project Overview
This project aims to predict an individual's **stress level** based on lifestyle factors such as smartphone usage, sleep patterns, caffeine intake, and physical activity. With the increasing use of digital devices, understanding the relationship between technology usage and mental health has become very important.

Using a dataset of **15,000 individuals**, this project applies **machine learning techniques** to analyze behavioral patterns and predict stress levels.

The final model is deployed as an interactive web application where users can input their lifestyle details and receive a predicted stress score.

---

## 🎯 Objectives
The main objectives of this project are:

- Analyze the relationship between smartphone usage and stress levels.
- Perform **Exploratory Data Analysis (EDA)** to identify patterns in the dataset.
- Apply **data preprocessing and feature engineering** techniques.
- Train multiple machine learning models.
- Evaluate models using appropriate performance metrics.
- Deploy the trained model as a **web application**.

---

## 📊 Dataset Description
The dataset contains information about **15,000 individuals** and includes lifestyle and behavioral features.

| Feature | Description |
|------|------|
| age | Age of the individual |
| gender | Gender of the individual |
| occupation | Profession |
| daily_screen_time_hours | Total daily smartphone usage |
| phone_usage_before_sleep_minutes | Phone usage before sleeping |
| sleep_duration_hours | Total hours of sleep |
| sleep_quality_score | Sleep quality rating |
| caffeine_intake_cups | Daily caffeine consumption |
| physical_activity_minutes | Daily exercise duration |
| notifications_received_per_day | Number of phone notifications |
| mental_fatigue_score | Mental fatigue level |
| stress_level | Target variable |

---

## 🔎 Exploratory Data Analysis
Exploratory Data Analysis was performed to understand data distribution and relationships between variables.

Some key visualizations used:

- Age distribution histogram
- Screen time distribution
- Sleep duration distribution
- Stress level distribution
- Correlation heatmap

EDA revealed strong relationships between **sleep quality, screen time, and stress levels**.

---

## ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Streamlit

---

## 🤖 Machine Learning Models
Several regression models were trained and evaluated:

- Decision Tree Regressor
- Random Forest Regressor
- Support Vector Regression (SVR)

A **machine learning pipeline** was used to integrate preprocessing and model training.

---

## 📈 Model Results

The **Support Vector Regression (SVR)** model achieved the best performance.

Model evaluation metrics:

- **RMSE:** 0.39
- **R² Score:** High predictive performance

This indicates that the model can accurately predict stress levels based on lifestyle and smartphone usage patterns.

---

## 🌐 Live Application

The trained model has been deployed as a web application.

🔗 **Live Demo:**  
https://stress-prediction-app.onrender.com/

Users can enter lifestyle information such as:

- Age
- Screen time
- Sleep duration
- Caffeine intake
- Physical activity
- Notifications received

The system then predicts the user's **stress level in real time**.

---

## 📂 Project Structure

stress-level-prediction-ml
│
├── app.py
├── stress_model.pkl
├── requirements.txt
├── dataset.csv
└── README.md


---

## 🚀 Future Improvements

Possible improvements for this project include:

- Integrating wearable device data
- Building a mobile application
- Implementing deep learning models
- Adding personalized stress management recommendations
- Real-time stress monitoring

---

## 👨‍💻 Author
Challa Naveen
Machine Learning Project  
Stress Level Prediction using Lifestyle and Smartphone Usage Data
