from fastapi import FastAPI, Path ,HTTPException
import json


app = FastAPI()

def load_data():
    with open('patients.json', 'r') as file:
        data = json.load(file)
    return data

@app.get("/")
def hello():
    return {"message": "Patients Management System with help of FastAPI"}

@app.get("/about")
def about():
    return {"message": "This is a simple FastAPI application for managing patient records."}

@app.get("/view")
def view():
    data = load_data()
    return data 

@app.get("/patient/{patient_id}")
def view_patient(patient_id: str = Path(..., description = "The ID of the patient to retrieve" , example="P001")):
    data = load_data()

    if patient_id in data:
        return data[patient_id]
    raise HTTPException(status_code=404, detail="Patient not found")