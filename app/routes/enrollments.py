from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.models.models import Student, Course
from app.schemas.schemas import EnrollmentRequest

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def enroll_student(request: EnrollmentRequest, db: Session = Depends(get_db)):
    student = db.query(Student).filter(Student.id == request.student_id).first()
    course = db.query(Course).filter(Course.id == request.course_id).first()
    if not student or not course:
        raise HTTPException(status_code=404, detail="Student or Course not found")
    student.courses.append(course)
    db.commit()
    return {"message": f"Student {student.name} enrolled in {course.title}"}