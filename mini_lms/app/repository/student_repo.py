from sqlalchemy.orm import Session, joinedload
from app.domain import models
from app.schemas import student_schema

class StudentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, student_id: int):
        # joinedload giúp lấy luôn thông tin Parent trong 1 câu lệnh SQL duy nhất
        return self.db.query(models.Student)\
            .options(joinedload(models.Student.parent))\
            .filter(models.Student.id == student_id)\
            .first()

    def create(self, student: student_schema.StudentCreate):
        db_student = models.Student(
            name=student.name,
            dob=student.dob,
            gender=student.gender,
            current_grade=student.current_grade,
            parent_id=student.parent_id
        )
        self.db.add(db_student)
        self.db.commit()
        self.db.refresh(db_student)
        return self.get_by_id(db_student.id) # Trả về kèm thông tin parent