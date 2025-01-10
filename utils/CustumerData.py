from pydantic import BaseModel,Field
from typing import List, Literal

class CustmerData(BaseModel):
    CreditScore: int=Field(description="Credit score of customer")
    Geography: Literal["France","Spain","Germany"]=Field(description="Customer's country")
    Gender:Literal["Male","Female"]=Field(description="Customer's Gender")
    Age: int = Field(description="Customer's age",ge=18,le=100)
    Tenure: int=Field(ge=0,le=10,description="Years as a customer (0-10)")
    Balance: float=Field(ge=0,description="Account balance")
    NumOfProducts: int=Field(ge=1,le=4,description="Number of bank products (1-4)")
    HasCrCard:Literal[0,1]=Field(description="Has credit card")
    IsActiveMember:Literal[0,1]=Field(description="Is active member")
    EstimatedSalary: float=Field(ge=0,description="Customer's EstimatedSalary")

