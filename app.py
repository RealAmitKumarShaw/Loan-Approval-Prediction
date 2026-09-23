import streamlit as st
import pandas as pd
import joblib


# -----------------------------
# Load Model and Feature Names
# -----------------------------

model = joblib.load("Models/loan_approval_model.pkl")
feature_names = joblib.load("Models/feature_names.pkl")


# -----------------------------
# Page Configuration
# -----------------------------

st.set_page_config(
    page_title="Loan Approval Prediction",
    page_icon="🏦",
    layout="centered"
)


# -----------------------------
# Title
# -----------------------------

st.title("🏦 Loan Approval Prediction")

st.write(
    "Enter the applicant details below to predict the loan approval status."
)


# -----------------------------
# Applicant Details
# -----------------------------

st.header("Applicant Information")


col1, col2 = st.columns(2)

with col1:

    no_of_dependents = st.number_input(
        "Number of Dependents",
        min_value=0,
        max_value=5,
        value=2,
        step=1
    )

    education = st.selectbox(
        "Education",
        ["Graduate", "Not Graduate"]
    )

    self_employed = st.selectbox(
        "Self Employed",
        ["No", "Yes"]
    )

    income_annum = st.number_input(
        "Annual Income",
        min_value=0,
        value=8000000,
        step=100000
    )

    loan_amount = st.number_input(
        "Loan Amount",
        min_value=0,
        value=20000000,
        step=100000
    )

    loan_term = st.number_input(
        "Loan Term (Years)",
        min_value=2,
        max_value=20,
        value=10,
        step=2
    )


with col2:

    cibil_score = st.number_input(
        "CIBIL Score",
        min_value=300,
        max_value=900,
        value=750,
        step=1
    )

    residential_assets_value = st.number_input(
        "Residential Assets Value",
        min_value=0,
        value=5000000,
        step=100000
    )

    commercial_assets_value = st.number_input(
        "Commercial Assets Value",
        min_value=0,
        value=3000000,
        step=100000
    )

    luxury_assets_value = st.number_input(
        "Luxury Assets Value",
        min_value=0,
        value=10000000,
        step=100000
    )

    bank_asset_value = st.number_input(
        "Bank Asset Value",
        min_value=0,
        value=7000000,
        step=100000
    )


# -----------------------------
# Prediction
# -----------------------------

if st.button("🔍 Predict Loan Status", use_container_width=True):

    input_data = pd.DataFrame({
        "no_of_dependents": [no_of_dependents],
        "income_annum": [income_annum],
        "loan_amount": [loan_amount],
        "loan_term": [loan_term],
        "cibil_score": [cibil_score],
        "residential_assets_value": [residential_assets_value],
        "commercial_assets_value": [commercial_assets_value],
        "luxury_assets_value": [luxury_assets_value],
        "bank_asset_value": [bank_asset_value],
        "education_ Not Graduate": [
            1 if education == "Not Graduate" else 0
        ],
        "self_employed_ Yes": [
            1 if self_employed == "Yes" else 0
        ]
    })


    # Ensure exact feature order
    input_data = input_data[feature_names]


    # Prediction
    prediction = model.predict(input_data)[0]

    probability = model.predict_proba(input_data)[0]

    rejected_probability = probability[0]
    approved_probability = probability[1]


    # -----------------------------
    # Display Result
    # -----------------------------

    st.subheader("Prediction Result")

    if prediction == 1:

        st.success("✅ Loan Status: APPROVED")

        st.write(
            f"Approved Probability: "
            f"{approved_probability:.2%}"
        )

    else:

        st.error("❌ Loan Status: REJECTED")

        st.write(
            f"Rejected Probability: "
            f"{rejected_probability:.2%}"
        )