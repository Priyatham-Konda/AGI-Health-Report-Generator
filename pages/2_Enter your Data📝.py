import requests
import streamlit as st
from streamlit_extras.switch_page_button import switch_page
from backend import gemini

# BMI Calculator
age = st.number_input("Enter Age", min_value=1, max_value=150)
weight = st.number_input("Enter Weight", min_value=10)
height = st.number_input("Enter Height (in cm)", min_value=1)
bmi = weight / ((height / 100) ** 2)
health_advice = ""
if bmi < 18.5:
    health_advice = "Underweight"
elif bmi < 25:
    health_advice = "Healthy"
elif bmi < 30:
    health_advice = "Overweight"
else:
    health_advice = "Obese"

rep_but = st.button("Generate Health Report")
report = ""
if rep_but:
    with st.spinner("Generating Report..."):
        gemini.prompt(age, bmi, health_advice)
    switch_page("Your Report")