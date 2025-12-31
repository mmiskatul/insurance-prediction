from fastapi import FastAPI 
from pydantic import BaseModel , Field ,computed_field 
from typing import Literal,Annotated
import pickle
import pandas as pd 


# import the ml model 
with open('model.pkl','rb') as f:
    model =pickle.load(f)
    
app=FastAPI() 

# pydantic model to validate incoming data 

class UserInput(BaseModel):
    age : Annotated[int,Field(...,gt=0,lt=120 ,description='Age of the User ')]
    weight: Annotated[float,Field(...,gt=0,description='Weight the User ')]
    height: Annotated[float,Field(...,gt=0,lt=2.5,description='Height of the User ')]
    income_lpa: Annotated[float,Field(...,gt=0,description='Annual Salary of the User in Lpa')]
    smoker: Annotated[bool,Field(...,description='Is the User are Smoker ')]
    city : Annotated[str,Field(...,description='The City User Live ')]
    occupation: Annotated[Literal['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job'],Field(...,description='User Occupation ')]
    