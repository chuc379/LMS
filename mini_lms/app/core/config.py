from pydantic_settings import BaseSettings, SettingsConfigDict

class Settings(BaseSettings):
    PROJECT_NAME: str = "Mini LMS System"
    # Giá trị mặc định này sẽ bị ghi đè nếu trong .env có DATABASE_URL
    DATABASE_URL: str = "postgresql://admin:password123@localhost:5432/mini_lms"
    
    # Sử dụng model_config cho các phiên bản Pydantic mới (v2)
    model_config = SettingsConfigDict(env_file=".env", extra="ignore")

settings = Settings()