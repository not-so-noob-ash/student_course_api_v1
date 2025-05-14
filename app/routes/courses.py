from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session
from typing import List
from app.database import SessionLocal
from app.models.models import Course
from app.schemas.schemas import CourseCreate, CourseOut, CourseOutWithStudents

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=CourseOut)
def create_course(course: CourseCreate, db: Session = Depends(get_db)):
    db_course = Course(title=course.title, description=course.description)
    db.add(db_course)
    db.commit()
    db.refresh(db_course)
    return db_course

@router.get("/{id}", response_model=CourseOutWithStudents)
def get_course(id: int, db: Session = Depends(get_db)):
    course = db.query(Course).filter(Course.id == id).first()
    if not course:
        raise HTTPException(status_code=404, detail="Course not found")
    return CourseOutWithStudents(
        id=course.id,
        title=course.title,
        description=course.description,
        students=[student.name for student in course.students]
    )

@router.get("/", response_model=List[CourseOut])
def list_courses(
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),
    db: Session = Depends(get_db)
):
    return db.query(Course).offset(offset).limit(limit).all()
