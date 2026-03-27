from sqlalchemy import Column, Integer, String, Date, ForeignKey, Time, TIMESTAMP, CheckConstraint, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from app.core.database import Base

class Parent(Base):
    __tablename__ = "parents"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20), unique=True, nullable=False)
    email = Column(String(100), unique=True)

    # Quan hệ: 1 Parent có nhiều Students
    students = relationship("Student", back_populates="parent", cascade="all, delete")


class Student(Base):
    __tablename__ = "students"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    dob = Column(Date)
    gender = Column(String(10))
    current_grade = Column(Integer)
    parent_id = Column(Integer, ForeignKey("parents.id", ondelete="CASCADE"))

    # Quan hệ ngược lại
    parent = relationship("Parent", back_populates="students")
    subscriptions = relationship("Subscription", back_populates="student")
    registrations = relationship("Registration", back_populates="student")


class Class(Base):
    __tablename__ = "classes"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), nullable=False)
    subject = Column(String(50))
    day_of_week = Column(Integer)  # 2: Thứ 2, 8: Chủ nhật
    time_slot = Column(Time, nullable=False)
    teacher_name = Column(String(100))
    max_students = Column(Integer, default=20)

    # Ràng buộc CHECK cho day_of_week
    __table_args__ = (
        CheckConstraint('day_of_week >= 2 AND day_of_week <= 8', name='check_day_of_week'),
    )

    registrations = relationship("Registration", back_populates="classroom")


class Subscription(Base):
    __tablename__ = "subscriptions"

    id = Column(Integer, primary_key=True, index=True)
    student_id = Column(Integer, ForeignKey("students.id"))
    package_name = Column(String(100))
    start_date = Column(Date, server_default=func.current_date())
    end_date = Column(Date)
    total_sessions = Column(Integer, nullable=False)
    used_sessions = Column(Integer, default=0)

    student = relationship("Student", back_populates="subscriptions")

    # Ràng buộc CHECK cho used_sessions
    __table_args__ = (
        CheckConstraint('used_sessions <= total_sessions', name='sessions_check'),
    )


class Registration(Base):
    __tablename__ = "class_registrations"

    id = Column(Integer, primary_key=True, index=True)
    class_id = Column(Integer, ForeignKey("classes.id"))
    student_id = Column(Integer, ForeignKey("students.id"))
    registration_date = Column(TIMESTAMP, server_default=func.now())

    # Quan hệ
    student = relationship("Student", back_populates="registrations")
    classroom = relationship("Class", back_populates="registrations")

    # Đảm bảo 1 học sinh không đăng ký trùng 1 lớp 2 lần
    __table_args__ = (
        UniqueConstraint('class_id', 'student_id', name='_class_student_uc'),
    )