from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.parent_repo import ParentRepository
from app.schemas.parent_schema import ParentCreate

class ParentService:
    def __init__(self, db: Session):
        self.repository = ParentRepository(db)

    def create_parent(self, parent_data: ParentCreate):
        # Kiểm tra logic: Số điện thoại đã tồn tại chưa?
        existing = self.repository.get_by_phone(parent_data.phone)
        if existing:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Số điện thoại phụ huynh đã tồn tại trên hệ thống."
            )
        return self.repository.create(parent_data)

    def get_parent_detail(self, parent_id: int):
        parent = self.repository.get_by_id(parent_id)
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy phụ huynh với ID {parent_id}"
            )
        return parent