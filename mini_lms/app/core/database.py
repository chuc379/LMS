from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.core.config import settings # Giả sử bạn có file config xử lý .env

# Lấy URL từ biến môi trường thông qua lớp Config
SQLALCHEMY_DATABASE_URL = settings.DATABASE_URL

# engine: Đối tượng quản lý kết nối thấp cấp
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, 
    # check_same_thread chỉ cần thiết cho SQLite
    connect_args={"check_same_thread": False} if "sqlite" in SQLALCHEMY_DATABASE_URL else {}
)

# SessionLocal: Factory để tạo ra các phiên làm việc (unit of work)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class để các Models ở tầng Domain kế thừa
Base = declarative_base()

# Dependency Injection: Cung cấp session cho tầng API
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()