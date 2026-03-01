import numpy as np 
import joblib 

scaler = joblib.load("scaler.pkl")

model = joblib.load("house_model.pkl")

def predict_price(rm, lstat, ptratio):
    """
    This function receives user inputs from the GUI,
    applies preprocessing, and returns the predicted price.
    """
    # Convert inputs into 2D array (required by sklearn)
    features = np.array([[rm, lstat, ptratio]])
    # Apply the SAME scaling used during training
    features_scaled = scaler.transform(features)
    # Predict using the trained model
    prediction = model.predict(features_scaled)
    price_dollars = prediction[0] * 1000
    return prediction[0]