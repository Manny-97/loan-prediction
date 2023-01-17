import requests

ride = {
    "Gender": 1,
    "Married": 0,
    "Education": 1,
    "Self_Employed": 0,
    "ApplicantIncome": 6300.0	,
    "CoapplicantIncome": 0.0,
    "LoanAmount": 500,
    "Loan_Amount_Term": 180,
    "Credit_History": 1.0,
    "Property_Area": 0,
    "Dependents": 0
}

url = 'http://127.0.0.1:9696/predict'

response = requests.post(url=url, json=ride)

print(response.json())