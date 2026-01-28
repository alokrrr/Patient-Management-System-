from fastapi import FastAPI, Path ,HTTPException, Query
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

@app.get('/sort')
def sort_patients(sort_by: str = Query(..., description="sort on the basic of the height,age or bmi"), 
  order: str = Query("asc", description="Order of sorting: asc or desc")):
    
    data = load_data()
    valid_sort_keys = {'height', 'age', 'bmi'}

    if sort_by not in valid_sort_keys:
        raise HTTPException(status_code=400, detail=f"Invalid sort_by value. Must be one of {valid_sort_keys}")

    reverse = order == "desc"

    try:
        sorted_data = dict(sorted(data.items(), key=lambda item: item[1][sort_by], reverse=reverse))
    except KeyError:
        raise HTTPException(status_code=400, detail=f"Sorting key '{sort_by}' not found in patient records.")

    return sorted_data
