from sqlalchemy.orm import Session
from app.domain import models
from app.schemas import parent_schema

class ParentRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_by_id(self, parent_id: int):
        return self.db.query(models.Parent).filter(models.Parent.id == parent_id).first()

    def get_by_phone(self, phone: str):
        return self.db.query(models.Parent).filter(models.Parent.phone == phone).first()

    def create(self, parent: parent_schema.ParentCreate):
        db_parent = models.Parent(
            name=parent.name,
            phone=parent.phone,
            email=parent.email
        )
        self.db.add(db_parent)
        self.db.commit()
        self.db.refresh(db_parent)
        return db_parent