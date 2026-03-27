from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.registration_schema import RegistrationCreate, RegistrationResponse
from app.services.registration_service import RegistrationService

router = APIRouter(prefix="/api/registrations", tags=["Registrations"])

@router.post("/classes/{class_id}/register", response_model=RegistrationResponse)
def register_to_class(
    class_id: int, 
    reg_in: RegistrationCreate, 
    db: Session = Depends(get_db)
):
    service = RegistrationService(db)
    return service.register_student(class_id, reg_in.student_id)

@router.delete("/{id}", status_code=status.HTTP_204_NO_CONTENT)
def cancel_registration(id: int, db: Session = Depends(get_db)):
    service = RegistrationService(db)
    service.cancel_registration(id)
    return None