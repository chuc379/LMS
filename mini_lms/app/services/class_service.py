from sqlalchemy.orm import Session
from app.repository.class_repo import ClassRepository
from app.schemas.class_schema import ClassCreate

class ClassService:
    def __init__(self, db: Session):
        self.repository = ClassRepository(db)

    def create_class(self, class_data: ClassCreate):
        # Bạn có thể thêm logic kiểm tra trùng lịch giáo viên ở đây nếu cần
        return self.repository.create(class_data)

    def list_classes_by_day(self, day: int):
        return self.repository.get_classes_by_day(day)