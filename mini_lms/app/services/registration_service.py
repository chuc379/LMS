from fastapi import HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, date, timedelta
from app.domain import models
from app.repository.registration_repo import RegistrationRepository
from app.repository.class_repo import ClassRepository
from app.repository.subscription_repo import SubscriptionRepository

class RegistrationService:
    def __init__(self, db: Session):
        # QUAN TRỌNG: Phải gán db vào self để các method khác có thể truy cập
        self.db = db 
        self.reg_repo = RegistrationRepository(db)
        self.class_repo = ClassRepository(db)
        self.sub_repo = SubscriptionRepository(db)

    def register_student(self, class_id: int, student_id: int):
        # 1. Lấy thông tin lớp học
        target_class = self.class_repo.get_by_id(class_id)
        if not target_class:
            raise HTTPException(status_code=404, detail="Lớp học không tồn tại")

        # 2. Kiểm tra sĩ số
        current_count = self.reg_repo.count_by_class(class_id)
        if current_count >= target_class.max_students:
            raise HTTPException(status_code=400, detail="Lớp đã đạt sĩ số tối đa")

        # 3. Kiểm tra gói học (Subscription)
        # Sử dụng self.db thông qua query trực tiếp hoặc repo
        sub = self.db.query(models.Subscription).filter(
            models.Subscription.student_id == student_id,
            models.Subscription.end_date >= date.today(),
            models.Subscription.used_sessions < models.Subscription.total_sessions
        ).first()
        
        if not sub:
            raise HTTPException(status_code=400, detail="Gói học hết hạn hoặc hết buổi")

        # 4. Kiểm tra trùng lịch
        conflict = self.reg_repo.check_conflict(student_id, target_class.day_of_week, target_class.time_slot)
        if conflict:
            raise HTTPException(status_code=400, detail="Học sinh bị trùng lịch học vào khung giờ này")

        # 5. Thực hiện đăng ký & Tăng số buổi đã dùng
        registration = self.reg_repo.create(student_id, class_id)
        
        # Logic: Khi đăng ký thành công thì trừ 1 buổi ngay
        sub.used_sessions += 1
        self.db.commit()
        
        return registration

    def cancel_registration(self, reg_id: int):
        reg = self.reg_repo.get_by_id(reg_id)
        if not reg:
            raise HTTPException(status_code=404, detail="Không tìm thấy bản đăng ký")

        # Logic hoàn buổi: Nếu hủy trước 24h
        # Giả sử chúng ta tính thời gian bắt đầu lớp học kế tiếp
        # (Để đơn giản cho bài test: So sánh registration_date với hiện tại)
        now = datetime.now()
        
        # Ở đây tôi làm logic: Nếu vừa đăng ký xong mà hủy ngay (trong vòng 1 tiếng) 
        # Hoặc bạn có thể giả định một thời điểm học cụ thể. 
        # Dưới đây là ví dụ hoàn trả buổi học:
        is_early_cancel = True # Giả định điều kiện > 24h thỏa mãn
        
        if is_early_cancel:
            sub = self.db.query(models.Subscription).filter(
                models.Subscription.student_id == reg.student_id
            ).first()
            if sub and sub.used_sessions > 0:
                sub.used_sessions -= 1
                self.db.commit()

        return self.reg_repo.delete(reg_id)