from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.subscription_schema import SubscriptionCreate, SubscriptionResponse
from app.services.subscription_service import SubscriptionService

router = APIRouter(prefix="/api/subscriptions", tags=["Subscriptions"])

@router.post("/", response_model=SubscriptionResponse, status_code=status.HTTP_201_CREATED)
def create_subscription(sub_in: SubscriptionCreate, db: Session = Depends(get_db)):
    """Khởi tạo gói học mới cho học sinh."""
    service = SubscriptionService(db)
    return service.init_subscription(sub_in)

@router.patch("/{id}/use", response_model=SubscriptionResponse)
def use_session(id: int, db: Session = Depends(get_db)):
    """Đánh dấu đã học 1 buổi (Giảm số buổi còn lại)."""
    service = SubscriptionService(db)
    return service.use_session(id)

@router.get("/{id}", response_model=SubscriptionResponse)
def get_subscription_status(id: int, db: Session = Depends(get_db)):
    """Xem chi tiết trạng thái gói học (Tổng vs Đã dùng)."""
    service = SubscriptionService(db)
    return service.get_status(id)