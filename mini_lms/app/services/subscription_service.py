from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.subscription_repo import SubscriptionRepository

class SubscriptionService:
    def __init__(self, db: Session):
        self.repository = SubscriptionRepository(db)

    def init_subscription(self, sub_data):
        return self.repository.create(sub_data)

    def use_session(self, sub_id: int):
        sub = self.repository.get_by_id(sub_id)
        if not sub:
            raise HTTPException(status_code=404, detail="Không tìm thấy gói học")
        
        if sub.used_sessions >= sub.total_sessions:
            raise HTTPException(status_code=400, detail="Gói học đã hết buổi, không thể sử dụng thêm")
            
        return self.repository.update_usage(sub_id)

    def get_status(self, sub_id: int):
        sub = self.repository.get_by_id(sub_id)
        if not sub:
            raise HTTPException(status_code=404, detail="Gói học không tồn tại")
        return sub