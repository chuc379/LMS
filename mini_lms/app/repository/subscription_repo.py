from sqlalchemy.orm import Session
from app.domain import models
from app.schemas import subscription_schema

class SubscriptionRepository:
    def __init__(self, db: Session):
        self.db = db

    def create(self, sub_data: subscription_schema.SubscriptionCreate):
        db_sub = models.Subscription(
            student_id=sub_data.student_id,
            package_name=sub_data.package_name,
            total_sessions=sub_data.total_sessions,
            end_date=sub_data.end_date,
            used_sessions=0
        )
        self.db.add(db_sub)
        self.db.commit()
        self.db.refresh(db_sub)
        return db_sub

    def get_by_id(self, sub_id: int):
        return self.db.query(models.Subscription).filter(models.Subscription.id == sub_id).first()

    def update_usage(self, sub_id: int):
        db_sub = self.get_by_id(sub_id)
        if db_sub:
            db_sub.used_sessions += 1
            self.db.commit()
            self.db.refresh(db_sub)
        return db_sub