from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine, Column, Integer, String

# 데이터베이스 연결
engine = create_engine("sqlite:///users.db", echo=True)

# 데이터베이스 연결 통로: 세션
SessionLocal = sessionmaker()

# Base 클래스 정의
Base = declarative_base()

# User 모델 정의: 사용자 이름을 저장하는 테이블
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)

SessionLocal = sessionmaker(bind=engine)

# 테이블 생성
Base.metadata.create_all(bind=engine)


##연습


def run_single():
    db = SessionLocal()

    # CREATE
    new_user = User(name="OZ_BE")
    db.add(new_user)
    db.commit()
    print("단일 사용자 추가:", new_user)
    
    # READ
    user = db.query(User).first()
    print("단일 사용자 찾음:", user)


    # UPDATE
    # DELETE
    db.close()