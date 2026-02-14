import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("energy_model.pkl")



st.title("Electricity Bill Prediction App -Dr.Chittranjan Pradhan")

# --------- User Inputs ---------

Family_Size = st.number_input("Family Size", min_value=1)
Monthly_Income = st.number_input("Monthly Income")
Appliances_Count = st.number_input("Appliances Count", min_value=0)
Month = st.number_input("Month (1-12)", min_value=1, max_value=12)
Gas_Usage = st.number_input("Gas Usage")

Electricity_Usage_kWh = st.number_input("Electricity Usage (kWh)")
Electricity_Rate_per_kWh = st.number_input("Electricity Rate per kWh")

# --------- Automatically Create Engineered Features ---------

Is_Summer = 1 if Month in [4,5,6] else 0
Is_Winter = 1 if Month in [11,12,1] else 0

Electricity_per_Person = Electricity_Usage_kWh / Family_Size if Family_Size != 0 else 0
Income_per_Person = Monthly_Income / Family_Size if Family_Size != 0 else 0
Electricity_per_Appliance = Electricity_Usage_kWh / Appliances_Count if Appliances_Count != 0 else 0
Income_x_Appliances = Monthly_Income * Appliances_Count

# --------- Prediction ---------

if st.button("Predict"):

    input_data = pd.DataFrame([{
        'Family_Size': Family_Size,
        'Monthly_Income': Monthly_Income,
        'Appliances_Count': Appliances_Count,
        'Month': Month,
        'Gas_Usage': Gas_Usage,
        'Is_Summer': Is_Summer,
        'Is_Winter': Is_Winter,
        'Electricity_Usage_kWh': Electricity_Usage_kWh,
        'Electricity_per_Person': Electricity_per_Person,
        'Income_per_Person': Income_per_Person,
        'Electricity_per_Appliance': Electricity_per_Appliance,
        'Income_x_Appliances': Income_x_Appliances,
        'Electricity_Rate_per_kWh': Electricity_Rate_per_kWh
    }])

    prediction = model.predict(input_data)

    st.success(f"Predicted Electricity Bill: {prediction[0]}")
