from fastapi import FastAPI , HTTPException
import pandas as pd
from app.schemas import  VehicleInput, SavingsInput, LoanInput
import joblib
app = FastAPI()

vehicle_price_prediction_preprocessor = joblib.load("../model/vehicle_preprocessor.pkl")
vehicle_price_prediction_model = joblib.load("../model/vehicle_price_model.pkl")
savings_prediction_pipeline = joblib.load("../model/savings_prediction_pipeline.pkl")
loan_affordablity_pipeline = joblib.load("../model/loan_affordability_prediction_pipeline.pkl")

@app.post("/get_vechicle_price")
def get_vechicle_price(vehicle:VehicleInput):
    input_df = pd.DataFrame([vehicle.dict()])
    processed = vehicle_price_prediction_preprocessor.transform(input_df)
    prediction = vehicle_price_prediction_model.predict(processed)
    return {
        "result" : float(prediction[0])
    }
@app.post("/get_optimal_savings")
def get_savings(savings: SavingsInput):
    input_df = pd.DataFrame([savings.dict()])
    prediction = savings_prediction_pipeline.predict(input_df)

    return {
        "predicted_savings": float(prediction[0])
    }

@app.post("/get_loan_affordability_result")
def get_loan_affordability(loan: LoanInput):
    input_df = pd.DataFrame([loan.dict()])
    prediction = loan_affordablity_pipeline.predict(input_df)

    return {
        "loan_affordability":"NO" if float(prediction[0]) == 1 else "YES"
    }

