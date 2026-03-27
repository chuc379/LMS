from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.student_schema import StudentCreate, StudentResponse
from app.services.student_service import StudentService

router = APIRouter(prefix="/api/students", tags=["Students"])

def get_student_service(db: Session = Depends(get_db)):
    return StudentService(db)

@router.post("/", response_model=StudentResponse, status_code=status.HTTP_201_CREATED)
def create_student(
    student_in: StudentCreate, 
    service: StudentService = Depends(get_student_service)
):
    """
    **Tạo Học sinh mới:**
    - Yêu cầu `parent_id` phải tồn tại.
    """
    return service.create_student(student_in)

@router.get("/{id}", response_model=StudentResponse)
def get_student(
    id: int, 
    service: StudentService = Depends(get_student_service)
):
    """
    **Xem chi tiết Học sinh:**
    - Trả về thông tin học sinh và thông tin Phụ huynh đi kèm.
    """
    return service.get_student_detail(id)