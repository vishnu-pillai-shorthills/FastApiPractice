from typing import Optional
from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

students = {
    1 : {
        "name" : "Vishnu",
        "age" : 22,
        "year": "year 12"
    }
} 

class Student(BaseModel):
    name: str
    age: int
    year: str

class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

@app.get("/")
def index():
    return {"name": "First Data"}

@app.get("/get-student/{id}")
def get_student(id : int = Path(..., description="The ID of the student data you require", gt=0, lt=3)):
    return students[id]

@app.get("/get-by-name")
def get_student(name: str=None):
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"Data not found"}


@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    if student_id in students:
        return {"Error": "Student Exists"}
    
    students[student_id] = student
    return students[student_id]

@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    if student_id not in students:
        return {"Error": "Data not found"}
    
    # students[student_id] = student
    if student.name != None:
        students[student_id]["name"] = student.name
    if student.age != None:
        students[student_id]["age"] = student.age
    if student.year != None:
        students[student_id]["year"] = student.year

    return students[student_id]


@app.delete("/delete-student/{student_id}")
def delete_student(student_id : int):
    if student_id not in students:
        return {"Error": "Data not found"}
    del students[student_id]
    return {"Message":"Data deleted Successfully"}