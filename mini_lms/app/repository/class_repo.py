from sqlalchemy.orm import Session
from app.domain import models
from app.schemas import class_schema

class ClassRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, class_data: class_schema.ClassCreate):
        db_class = models.Class(
            name=class_data.name,
            subject=class_data.subject,
            day_of_week=class_data.day_of_week,
            time_slot=class_data.time_slot,
            teacher_name=class_data.teacher_name,
            max_students=class_data.max_students
        )
        self.db.add(db_class)
        self.db.commit()
        self.db.refresh(db_class)
        return db_class

    def get_classes_by_day(self, day: int):
        return self.db.query(models.Class).filter(models.Class.day_of_week == day).all()

    def get_by_id(self, class_id: int):
        return self.db.query(models.Class).filter(models.Class.id == class_id).first()