# 🎓 TeenUp Mini LMS - Product Builder Assignment

> Một hệ thống Quản lý Học tập (LMS) tinh gọn, tập trung vào tối ưu hóa luồng đăng ký lớp học và quản lý Subscription thông minh.

---

## 🚀 Tính năng cốt lõi (Core Features)

### 1. Quản lý Hồ sơ & Liên kết (Profiles)
* **Identity:** Khởi tạo và liên kết chặt chẽ thông tin **Phụ huynh (Parents)** & **Học sinh (Students)**.
* **Real-time Classes:** Hiển thị và quản lý danh sách lớp học theo thời gian thực.

### 2. Nghiệp vụ Đăng ký Thông minh (Smart Registration)
* **Conflict Prevention:** Hệ thống tự động chặn nếu học sinh đăng ký 2 lớp có cùng khung giờ trong cùng 1 ngày.
* **Capacity Control:** Tự động kiểm tra sĩ số tối đa (`max_students`) trước khi cho phép ghi danh.
* **Subscription Validation:** Chỉ cho phép đăng ký nếu gói học còn hạn và còn số buổi khả dụng (`used_sessions < total_sessions`).

### 3. Logic Hủy lịch & Hoàn buổi (Cancellation Logic)
* **Flexible Refund:** Hủy trước **> 24h** sẽ tự động hoàn trả 1 buổi vào gói học.
* **Strict Policy:** Hủy sát giờ (**< 24h**) sẽ xóa bản đăng ký nhưng không hoàn trả buổi học để đảm bảo vận hành lớp.

---

## 🛠 Tech Stack

| Thành phần | Công nghệ sử dụng |
| :--- | :--- |
| **Backend** | FastAPI (Python 3.11), SQLAlchemy ORM, Pydantic |
| **Database** | PostgreSQL 15 |
| **Frontend** | Next.js 15 (Turbopack), Tailwind CSS v4 |
| **DevOps** | Docker, Docker Compose |

---

## 📦 Hướng dẫn khởi chạy nhanh (Quick Start)

**Yêu cầu:** Máy đã cài đặt **Docker** & **Docker Compose**.

### 1. Clone dự án
```bash
git clone [https://github.com/chuc379/LMS.git](https://github.com/chuc379/LMS.git)
cd LMS
2. Khởi chạy hệ thống
Bash
docker-compose up --build
3. Truy cập các cổng dịch vụ
Frontend: http://localhost:3000

Swagger UI (API Docs): http://localhost:5001/swagger

Database: localhost:5432 (User: admin, Pass: password123)

📂 Cấu trúc dự án (Project Structure)
Plaintext
.
├── mini_lms/           # Backend: FastAPI App (Clean Architecture)
│   ├── app/            # Core logic, Models, Schemas, Repositories
│   ├── main.py         # Entry point
│   └── Dockerfile      # Backend Containerization
├── FE/                 # Frontend: Next.js 15 App
│   ├── components/     # UI Modular Components (Forms, Calendar, Modals)
│   ├── app/            # App Router logic
│   └── Dockerfile      # Frontend Containerization
├── docker-compose.yml  # Multi-container Orchestration
└── README.md           # Documentation
🧪 Kịch bản kiểm thử (Test Cases)
Để kiểm tra logic nghiệp vụ trên Swagger UI, hãy thực hiện theo luồng sau:

Profiles: Tạo Parent & Student để lấy student_id.

Credit: Tạo 1 Subscription (ví dụ: 10 buổi) cho học sinh đó.

Schedule: Tạo lớp học vào Thứ Hai, lúc 08:00.

Register: Thực hiện đăng ký học sinh vào lớp.

Logic Check: Thử đăng ký lại học sinh đó vào một lớp khác cũng lúc 08:00 Thứ Hai -> Hệ thống trả về lỗi 400 Bad Request (Trùng lịch).

Author: Chương - Product Builder Applicant


---

### 🏁 Chốt hạ để nộp bài
1. Dán nội dung trên vào file `README.md`.
2. Chạy lệnh đẩy lên GitHub:
   ```bash
   git add README.md
   git commit -m "docs: finalize clean readme documentation"
   git push origin main
