from fastapi import APIRouter, Depends, Query, status
from sqlalchemy.orm import Session
from typing import List
from app.core.database import get_db
from app.schemas.class_schema import ClassCreate, ClassResponse
from app.services.class_service import ClassService

router = APIRouter(prefix="/api/classes", tags=["Classes"])

def get_class_service(db: Session = Depends(get_db)):
    return ClassService(db)

@router.post("/", response_model=ClassResponse, status_code=status.HTTP_201_CREATED)
def create_class(
    class_in: ClassCreate, 
    service: ClassService = Depends(get_class_service)
):
    """
    **Tạo lớp học mới:**
    - day_of_week: Từ 2 (Thứ 2) đến 8 (Chủ nhật).
    - time_slot: Định dạng HH:MM (VD: 08:30).
    """
    return service.create_class(class_in)

@router.get("/", response_model=List[ClassResponse])
def get_classes_by_day(
    day: int = Query(..., ge=2, le=8, description="Thứ trong tuần (2-8)"),
    service: ClassService = Depends(get_class_service)
):
    """
    **Lấy danh sách lớp học theo ngày:**
    - Trả về tất cả các lớp mở vào thứ được chọn.
    """
    return service.list_classes_by_day(day)