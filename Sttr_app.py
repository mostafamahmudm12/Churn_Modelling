import streamlit as st
import pandas as pd
from utils.inference import predict_new
from utils.config import APP_NAME,VERSION,Preprocessor,Forest_Models
from utils.CustumerData import CustmerData

# Configure the Streamlit page
st.set_page_config(
    page_title=f"{'Churn-Detection'} v{1.0}",
    page_icon="🏦",
    layout="wide"
)

def main():
    # Header
    st.title(f"{APP_NAME}")
    st.markdown(f"Version: {VERSION}")
    
    # Sidebar for model selection
    model_type = st.sidebar.selectbox(
        "Select Model",
        ["Random Forest", "XGBoost"]
    )
    
    # Main form for customer data input
    st.subheader("Enter Customer Data")
    
    with st.form("prediction_form"):
        col1, col2, col3 = st.columns(3)
        
        with col1:
            credit_score = st.number_input(
                "Credit Score",
                min_value=300,
                max_value=850,
                help="Customer's credit score"
            )
            
            geography = st.selectbox(
                "Geography",
                options=["France", "Spain", "Germany"],
                help="Customer's country"
            )
            
            gender = st.selectbox(
                "Gender",
                options=["Male", "Female"],
                help="Customer's gender"
            )
        
        with col2:
            age = st.number_input(
                "Age",
                min_value=18,
                max_value=100,
                help="Customer's age"
            )
            
            tenure = st.number_input(
                "Tenure",
                min_value=0,
                max_value=10,
                help="Years as a customer (0-10)"
            )
            
            balance = st.number_input(
                "Balance",
                min_value=0.0,
                help="Account balance"
            )
        
        with col3:
            num_products = st.number_input(
                "Number of Products",
                min_value=1,
                max_value=4,
                help="Number of bank products (1-4)"
            )
            
            has_credit_card = st.selectbox(
                "Has Credit Card",
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Does the customer have a credit card?"
            )
            
            is_active = st.selectbox(
                "Is Active Member",
                options=[0, 1],
                format_func=lambda x: "Yes" if x == 1 else "No",
                help="Is the customer an active member?"
            )
            
            estimated_salary = st.number_input(
                "Estimated Salary",
                min_value=0.0,
                help="Customer's estimated salary"
            )
        
        # Submit button
        submit_button = st.form_submit_button("Predict")
        
        if submit_button:
            try:
                # Create CustmerData instance
                customer_data = CustmerData(
                    CreditScore=credit_score,
                    Geography=geography,
                    Gender=gender,
                    Age=age,
                    Tenure=tenure,
                    Balance=balance,
                    NumOfProducts=num_products,
                    HasCrCard=has_credit_card,
                    IsActiveMember=is_active,
                    EstimatedSalary=estimated_salary
                )
                
                # Select model based on user choice
                selected_model = Forest_Models if model_type == "Random Forest" else Forest_Models  # Replace second Forest_Models with XGBoost model when available
                
                # Make prediction
                result = predict_new(
                    data=customer_data,
                    preprocessor=Preprocessor,
                    model=selected_model
                )
                
                # Display results
                st.success("Prediction Complete!")
                
                # Create a nice display of the results
                st.subheader("Prediction Results")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.metric("Prediction", result.get("prediction", "N/A"))
                
                with col2:
                    if "probability" in result:
                        st.metric("Probability", f"{result['probability']:.2%}")
                
                # Show full result details in expandable section
                with st.expander("See detailed results"):
                    st.json(result)
                
            except Exception as e:
                st.error(f"An error occurred during prediction: {str(e)}")

    # Information about the app
    with st.expander("About this app"):
        st.write("""
        This application predicts customer behavior using machine learning models.
        You can choose between Random Forest and XGBoost models from the sidebar.
        
        Fill in all the required customer information:
        - Credit Score (300-850)
        - Geography (France, Spain, or Germany)
        - Gender (Male or Female)
        - Age (18-100)
        - Tenure (0-10 years)
        - Balance (account balance)
        - Number of Products (1-4)
        - Credit Card Status (Yes/No)
        - Active Member Status (Yes/No)
        - Estimated Salary
        """)

if __name__ == "__main__":
    main()