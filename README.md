# Customer Churn Prediction

This project is a Streamlit application that predicts customer churn using a trained machine learning model. The application allows users to input customer-specific data (e.g., usage statistics, and service plans) and receive predictions on whether the customer is likely to churn. This tool is particularly useful for businesses that want to identify customers at risk and take preventive measures to retain them.

---

## Features
- **Interactive Input**: Users can adjust sliders and radio buttons to simulate different customer scenarios.
- **Real-Time Predictions**: The app uses a pre-trained machine learning model to predict customer churn instantly.
- **User-Friendly Interface**: Built with Streamlit, offering a clean and intuitive UI.
- **Data-Driven Insights**: Uses customer metrics like total charges, call minutes, and service interactions to make predictions.

---

## Technologies Used
- **Python**: Core programming language.
- **Streamlit**: For building an interactive web application.
- **Scikit-learn**: For preprocessing the data and training the machine learning model.
- **Joblib**: For saving and loading the trained model and scaler.
- **NumPy**: For numerical computations.

---

## Input Features
- **Total Day Charge**: The total charges for daytime usage.
- **Total Day Minutes**: Total minutes of daytime usage.
- **Number of Customer Service Calls**: Number of times the customer contacted customer service.
- **International Plan**: Whether the customer has subscribed to an international plan.
- **Total Evening Charge**: The total charges for evening usage.

---

## Future Enhancements
- Add more customer features to improve prediction accuracy.
- Integrate visualizations for customer churn trends.
- Include an option to upload bulk customer data for batch predictions.
- Deploy the app to **Streamlit Cloud** or **Heroku** for broader accessibility.
