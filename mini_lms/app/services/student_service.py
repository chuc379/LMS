from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from app.repository.student_repo import StudentRepository
from app.repository.parent_repo import ParentRepository
from app.schemas.student_schema import StudentCreate

class StudentService:
    def __init__(self, db: Session):
        self.student_repo = StudentRepository(db)
        self.parent_repo = ParentRepository(db) # Để kiểm tra parent_id có tồn tại không

    def create_student(self, student_data: StudentCreate):
        # Logic: Phải có Phụ huynh tồn tại mới cho tạo học sinh
        parent = self.parent_repo.get_by_id(student_data.parent_id)
        if not parent:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy Phụ huynh với ID {student_data.parent_id}"
            )
        return self.student_repo.create(student_data)

    def get_student_detail(self, student_id: int):
        student = self.student_repo.get_by_id(student_id)
        if not student:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail=f"Không tìm thấy Học sinh với ID {student_id}"
            )
        return student