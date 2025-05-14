from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.models import Student
from app.schemas.schemas import StudentCreate, StudentOut, StudentOutWithCourses

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=StudentOut)
def create_student(student: StudentCreate, db: Session = Depends(get_db)):
    db_student = Student(name=student.name, email=student.email)
    db.add(db_student)
    db.commit()
    db.refresh(db_student)
    return db_student

@router.get("/{id}", response_model=StudentOutWithCourses)
def get_student(id: int, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == id).first()
    if not student:
        raise HTTPException(status_code=404, detail="Student not found")
    return StudentOutWithCourses(
        id=student.id,
        name=student.name,
        email=student.email,
        courses=[course.title for course in student.courses]
    )

@router.get("/", response_model=List[StudentOut])
def list_students(
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    students = db.query(Student).offset(offset).limit(limit).all()
    return students
