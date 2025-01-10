
from .CustumerData import CustmerData
import pandas as pd

def predict_new(data: CustmerData, preprocessor, model):
    try:
        # Convert input data to a DataFrame
        df = pd.DataFrame([data.dict()])  # Use dict() if CustmerData is a Pydantic model
        
        # Debugging: Log the data frame
        print(f"Input DataFrame: {df}")

        # Transform the data using the preprocessor
        x_processed = preprocessor.transform(df)
        
        # Debugging: Log the transformed data
        print(f"Transformed Data: {x_processed}")

        # Predict churn and probabilities
        y_prediction = model.predict(x_processed)
        t_prob = model.predict_proba(x_processed)

        # Debugging: Log the predictions
        print(f"Prediction: {y_prediction}, Probabilities: {t_prob}")

        # Return the results in a structured format
        return {
            "churn_prediction": bool(y_prediction[0]),
            "churn_probability": float(t_prob[0][1])
        }

    except AttributeError as e:
        raise ValueError(f"Attribute error: {e}. Check the input structure or model methods.")
    except Exception as e:
        raise ValueError(f"An error occurred during prediction: {e}")
    