import streamlit as st
import numpy as np
import joblib

# Load the trained model and scaler
try:
    model = joblib.load('/Users/sahilgulati/PycharmProjects/Churn predictor/app/trained-model/churn_model.pkl')
    scaler = joblib.load('/Users/sahilgulati/PycharmProjects/Churn predictor/app/trained-model/scaler.pkl')
except Exception as e:
    st.error(f"Error loading model or scaler: {e}")
    st.stop()

# Streamlit UI
st.title("Customer Churn Prediction")

# Input features
total_day_charge = st.slider("Total Day Charge ($)", 0.0, 100.0, 10.0)
total_day_minutes = st.slider("Total Day Minutes", 0, 500, 50)
number_customer_service_calls = st.slider("Number of Customer Service Calls", 0, 10, 3)
international_plan_yes = st.radio("International Plan", ['Yes', 'No'])
total_eve_charge = st.slider("Total Evening Charge ($)", 0.0, 100.0, 10.0)

# Convert categorical input
international_plan_yes = 1 if international_plan_yes == 'Yes' else 0

# Prepare input data
try:
    input_data = np.array([[total_day_charge, total_day_minutes, number_customer_service_calls, international_plan_yes, total_eve_charge]])
    full_input_data = np.zeros((1, 69))  # Placeholder for 69 features
    full_input_data[0, :5] = input_data

    # Debug log for input data
    print("Full Input Data:", full_input_data)
except Exception as e:
    st.error(f"Error preparing input data: {e}")
    st.stop()

# Prediction logic
if st.button("Predict Churn"):
    try:
        # Scale the input
        scaled_input_data = scaler.transform(full_input_data)
        print("Scaled Input Data:", scaled_input_data)

        # Prediction (using class labels directly)
        prediction = model.predict(scaled_input_data)
        print("Prediction:", prediction)

        prediction_label = [np.argmax(prediction)]
        # Display result
        if prediction_label[0] == 1:
            st.success("The customer is likely to churn.")
        else:
            st.success("The customer is likely to stay loyal.")

    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")

