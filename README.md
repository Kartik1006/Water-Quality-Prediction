# RiverWatch: A Predictive Water Quality Monitoring System

[![Python Version](https://img.shields.io/badge/Python-3.9+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit App](https://img.shields.io/badge/Streamlit-App-red?logo=streamlit&logoColor=white)](https://streamlit.io/)

---
A complete end-to-end Machine Learning project that forecasts key water quality indicators for the Southern Bug River using a time-series machine learning model and a deployed web application.

---

## Table of Contents
- [Project Overview](#project-overview)
- [The Problem: From Reactive to Proactive](#the-problem-from-reactive-to-proactive)
- [The Solution: Time-Series Forecasting](#the-solution-time-series-forecasting)
- [Key Features](#key-features)
- [Tech Stack](#tech-stack)
- [Model Performance](#model-performance)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
- [How to Run](#how-to-run)
- [Future Improvements](#future-improvements)

## Project Overview

**RiverWatch** is a proof-of-concept system designed to predict future water quality based on historical data. The project tackles the challenge of forecasting multiple environmental parameters simultaneously (`O2`, `NO3`, `NO2`, `SO4`, `PO4`, `CL`) for various monitoring stations.

The core of the project is a `MultiOutputRegressor` using a `RandomForestRegressor` engine, enhanced with sophisticated **time-series feature engineering**. This allows the model to understand trends and seasonality, moving beyond a simple "lookup" to a genuine forecasting tool. The final model is deployed via a local Flask web application.

## The Problem: From Reactive to Proactive

Traditional water quality monitoring relies on manual sampling and lab analysis. This approach is:
- **Reactive:** Problems are often discovered long after they begin.
- **Slow:** Data lag can be days or weeks.
- **Resource-Intensive:** High costs limit the frequency of testing.

This project explores a shift to a **proactive, data-driven model**, enabling authorities to anticipate potential issues and make more informed decisions.

## The Solution: Time-Series Forecasting

Initial attempts to model the data using only `station ID` and `date` failed, resulting in negative R² scores. This indicated that the model lacked the necessary historical context.

The successful solution involved a deep dive into **time-series feature engineering**:
1.  **Lag Features:** We gave the model a "memory" by providing it with the pollutant levels from previous months (e.g., the value 1, 3, and 6 months ago).
2.  **Rolling Window Features:** We provided trend information by calculating statistics like the mean and standard deviation over a recent period (e.g., the last 3 months).

This transformed the model from a failed prototype into a functional forecaster with legitimate predictive power.

## Key Features
- **Multi-Target Prediction:** Forecasts 6 different water quality indicators simultaneously.
- **Time-Series Intelligence:** Utilizes historical data lags and rolling windows to capture trends.
- **Station-Specific Models:** The `station ID` is used as a feature to learn the unique baseline for each location.
- **Web Interface:** A simple Streamlit application allows users to select a station and date to receive a forecast.
- **End-to-End Pipeline:** Includes data preprocessing, feature engineering, model training, and deployment scripts.

## Tech Stack
- **Language:** Python 3.9+
- **Data Science:** Pandas, NumPy, Scikit-learn
- **Web Framework:** Streamlit
- **Model Persistence:** Joblib

## Model Performance
The time-series model showed a dramatic improvement over the initial approach. The R-squared (R²) scores on the unseen test set are as follows:

| Pollutant              | R-squared (R²) Score |
|:-----------------------|:--------------------:|
| **SO₄ (Sulfate)**      | **0.83**             |
| **Cl (Chloride)**      | **0.91**             |
| **PO₄ (Phosphate)**    | **0.59**             |
| **NO₂ (Nitrite)**      | **-2.61**             |
| **O₂ (Dissolved Oxygen)** | **0.24**             |
| **NO₃ (Nitrate)**      | **0.69**             |

The strong performance on `Cl` and `SO₄` is a particular highlight.

## Project Structure
```
.
├── app.py                  # The main Streamlit application file
├── prediction_model.pkl    # The saved, trained machine learning model
├── model_columns.pkl       # The list of feature columns required by the model
├── Project.ipynb           # Jupyter Notebook with data exploration and model training
├── requirements.txt        # List of Python dependencies
└── README.md               # You are here
```

## Setup and Installation

Follow these steps to set up the project locally.

**1. Clone the repository:**
```bash
git clone https://github.com/[YourUsername]/RiverWatch.git
cd RiverWatch
```

**2. Create a virtual environment (recommended):**
```bash
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

**3. Install the required dependencies:**
```bash
pip install -r requirements.txt
```
*(Note: You may need to generate the `prediction_model.pkl` and `model_columns.pkl` files first by running the Jupyter Notebook if they are not included in the repository.)*

## How to Run

**1. Run the Streamlit Application:**
From the root directory of the project, execute the following command:
```bash
streamlit run app.py
```

**2. Access the Web Interface:**
Open your web browser and navigate to:
```
  Local URL: http://localhost:8501
  Network URL: http://192.168.117.123:8501
```
You will see the user interface where you can input a Station ID, Year, and Month to get a water quality forecast.

## Future Improvements
This project serves as a strong foundation. Future work could include:
- **Long-Range Forecasting:** Implement an iterative prediction loop to forecast further into the future.
- **Incorporate External Data:** Add weather data (temperature, rainfall) as features to improve accuracy.
- **Advanced Time-Series Models:** Experiment with specialized models like LSTMs or Facebook's Prophet.
- **Cloud Deployment:** Deploy the Streamlit application to a cloud service like Heroku or AWS for public access.
- **Data Visualization:** Add charts to the web interface to show historical trends alongside the predictions.
