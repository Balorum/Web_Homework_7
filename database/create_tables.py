from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import DateTime
from create_base import Base

class Group(Base):
    __tablename__ = "groups"
    id = Column(Integer, primary_key=True)
    group_number = Column(Integer, unique=True, nullable=False)

class Teacher(Base):
    __tablename__ = "teachers"
    id = Column(Integer, primary_key=True)
    teacher_name = Column(String(100), unique=True, nullable=False)

class Subject(Base):
    __tablename__ = "subjects"
    id = Column(Integer, primary_key=True)
    subject_name = Column(String(100), nullable=False, unique=True)
    teacher_id = Column(Integer, ForeignKey(Teacher.id, ondelete="CASCADE", onupdate="CASCADE"))

class Student(Base):
    __tablename__ = "students"
    id = Column(Integer, primary_key=True)
    student_name = Column(String(100), nullable=False, unique=True)
    group_id = Column(Integer, ForeignKey(Group.id, ondelete="CASCADE", onupdate="CASCADE"))
    
class Mark(Base):
    __tablename__ = "marks"
    id = Column(Integer, primary_key=True)
    student_id = Column(Integer, ForeignKey(Student.id, ondelete="CASCADE", onupdate="CASCADE"))
    subject_id = Column(Integer, ForeignKey(Subject.id, ondelete="CASCADE", onupdate="CASCADE"))
    mark = Column(Integer, nullable=False)
    date_of = Column(DateTime, nullable=False)