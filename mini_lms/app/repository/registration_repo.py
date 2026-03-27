from sqlalchemy.orm import Session
from app.domain import models
from datetime import datetime

class RegistrationRepository:
    def __init__(self, db: Session):
        self.db = db

    def count_by_class(self, class_id: int):
        return self.db.query(models.Registration).filter(models.Registration.class_id == class_id).count()

    def check_conflict(self, student_id: int, day: int, time_slot):
        return self.db.query(models.Registration).join(models.Class).filter(
            models.Registration.student_id == student_id,
            models.Class.day_of_week == day,
            models.Class.time_slot == time_slot
        ).first()

    def create(self, student_id: int, class_id: int):
        db_reg = models.Registration(student_id=student_id, class_id=class_id)
        self.db.add(db_reg)
        self.db.commit()
        self.db.refresh(db_reg)
        return db_reg

    def get_by_id(self, reg_id: int):
        return self.db.query(models.Registration).filter(models.Registration.id == reg_id).first()

    def delete(self, reg_id: int):
        db_reg = self.get_by_id(reg_id)
        if db_reg:
            self.db.delete(db_reg)
            self.db.commit()
        return db_reg