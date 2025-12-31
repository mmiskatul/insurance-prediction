import streamlit as st 
import requests

API_URL = "http://localhost:8000/predict"

st.title("Insurance Premium Category Prediction")
st.markdown("Enter your details below: ")


#input fields 
age = st.number_input("Age",min_value=1,max_value=119,value=30)
weight =st.number_input("Weight (Kg)",min_value=1.0,max_value=65.0)
height =st.number_input("Height ",min_value=0.5,max_value=2.5,value=1.7)
incom_lpa =st.number_input("Annual Income (LPA)",min_value=0.1,value=10.0)
smoker =st.selectbox('Are your a Smoker?',options=[True,False])
city =st.text_input("City",value="Mumbai")
occupation = st.selectbox(
    "Occupation",
    options=['retired', 'freelancer', 'student', 'government_job',
       'business_owner', 'unemployed', 'private_job']
)