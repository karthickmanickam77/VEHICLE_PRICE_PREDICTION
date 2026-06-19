from pydantic import BaseModel

class VehicleInput(BaseModel):
    make_year:int
    mileage_kmpl:float
    engine_cc:int 
    fuel_type:str
    owner_count:int
    brand:str 
    transmission:str
    color:str
    service_history:str 
    accidents_reported:int 
    insurance_valid:str

class SavingsInput(BaseModel):
    Income: float
    Age: int
    Dependents: int
    Occupation: str
    City_Tier: str
    Rent: float
    Loan_Repayment: float
    Insurance: float
    Groceries: float
    Transport: float
    Eating_Out: float
    Entertainment: float
    Utilities: float
    Healthcare: float
    Education: float
    Miscellaneous: float


class LoanInput(BaseModel):
    person_age: int
    person_income: int
    person_home_ownership: str
    person_emp_length: float
    loan_amnt: int
    loan_int_rate: float
    loan_percent_income: float   # EMI burden, not raw ratio
    cb_person_default_on_file: str
    cb_person_cred_hist_length: int