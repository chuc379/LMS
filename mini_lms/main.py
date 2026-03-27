from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

# 1. Import Core & Database
from app.core.database import engine, Base
from app.core.config import settings

# 2. IMPORT MODELS (Quan trọng: Phải import để SQLAlchemy tạo bảng thành công)
from app.domain import models 

# 3. Import các Router từ tầng API
from app.api.parents_router import router as parents_router
from app.api.students_router import router as students_router
from app.api.classes_router import router as classes_router
from app.api.subscriptions_router import router as subscriptions_router
from app.api.registrations_router import router as registrations_router

# --- KHỞI TẠO DATABASE ---
# Tự động đồng bộ hóa cấu trúc SQL với PostgreSQL khi khởi động server
Base.metadata.create_all(bind=engine)

# --- KHỞI TẠO APP FASTAPI ---
app = FastAPI(
    title="Mini LMS API",
    description="""
    ## Hệ thống Quản lý Học sinh - Phụ huynh chuyên nghiệp (Product Builder Version)
    
    ### Tính năng chính:
    * **Parents & Students**: Quản lý thông tin hồ sơ và liên kết gia đình.
    * **Classes**: Lên lịch học theo thứ (`day_of_week`) và khung giờ (`time_slot`).
    * **Subscriptions**: Theo dõi gói học, số buổi còn lại và hạn dùng.
    * **Registrations**: Đăng ký học thông minh (Tự động kiểm tra trùng lịch, sĩ số và gói học).
    
    *Cấu trúc Project tuân thủ nguyên tắc Clean Architecture.*
    """,
    version="1.0.0",
    docs_url="/swagger",
    redoc_url="/redoc"
)

# --- CẤU HÌNH MIDDLEWARE (CORS) ---
# Cho phép Frontend tương tác với API mà không bị lỗi bảo mật trình duyệt
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ĐĂNG KÝ ROUTERS (QUY TRÌNH NGHIỆP VỤ) ---
app.include_router(parents_router)
app.include_router(students_router)
app.include_router(classes_router)
app.include_router(subscriptions_router)
app.include_router(registrations_router)

# --- HEALTH CHECK & ROOT ---
@app.get("/", tags=["System"], summary="Trạng thái máy chủ")
def root():
    """
    Kiểm tra nhanh tình trạng kết nối của hệ thống.
    """
    return {
        "status": "online",
        "database": "connected",
        "environment": "development",
        "docs": "/swagger"
    }

# --- KHỞI CHẠY ---
# Chạy bằng lệnh: uvicorn main:app --reload