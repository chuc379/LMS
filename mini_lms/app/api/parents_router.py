from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.parent_schema import ParentCreate, ParentResponse
from app.services.parent_service import ParentService

router = APIRouter(prefix="/api/parents", tags=["Parents"])

# Hàm helper để khởi tạo service
def get_parent_service(db: Session = Depends(get_db)):
    return ParentService(db)

@router.post(
    "/", 
    response_model=ParentResponse, 
    status_code=status.HTTP_201_CREATED,
    responses={400: {"description": "Số điện thoại đã tồn tại"}}
)
def create_parent(
    parent_in: ParentCreate, 
    service: ParentService = Depends(get_parent_service)
):
    """
    **Tạo Phụ huynh mới:**
    - Yêu cầu: Tên, Số điện thoại (duy nhất).
    - Logic: Kiểm tra trùng số điện thoại trước khi lưu.
    """
    return service.create_parent(parent_in)

@router.get(
    "/{id}", 
    response_model=ParentResponse,
    responses={404: {"description": "Không tìm thấy phụ huynh"}}
)
def get_parent(
    id: int, 
    service: ParentService = Depends(get_parent_service)
):
    """
    **Lấy chi tiết Phụ huynh:**
    - Trả về thông tin cơ bản của Phụ huynh theo ID.
    """
    return service.get_parent_detail(id)