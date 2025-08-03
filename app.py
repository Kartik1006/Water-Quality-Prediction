import pandas as pd
import numpy as np
import joblib
import pickle
import streamlit as st

model = joblib.load("prediction_model.pkl")
modelc = joblib.load("model_columns.pkl")

# Create UI
st.title("Water pollutants prediction")
st.write("Predict water pollutants based on year, month and station id.")

year = st.number_input("Enter year:", min_value=2000, max_value=2047, value=2025, step=1, format="%d")
month = st.number_input("Enter month:", min_value=1, max_value=12)
station_id = st.number_input("Enter station id:", min_value=1, max_value=22)

if st.button("Predict"):
    idf = pd.DataFrame({"year": [year], "month": [month], "id": [station_id]})
    iencoded = pd.get_dummies(idf, columns=['id'])

    for col in modelc:
        if col not in iencoded.columns:
            iencoded[col] = 0
        iencoded = iencoded[[col for col in modelc if col in iencoded.columns]]

    pred_pollutants = model.predict(iencoded)[0]
    pollutants = ['O2', 'NO3', 'NO2', 'SO4', 'PO4', 'CL']

    st.subheader(f"Predicted pollutants (for {month}/{year} with station id: {station_id})")

    pvalues = {}
    for p,val in zip(pollutants, pred_pollutants):
        st.write(f'{p}: {val:.2f}')
    print(iencoded.columns.tolist())
    print()
    print(modelc)

