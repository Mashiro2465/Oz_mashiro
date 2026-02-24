from sqlalchemy import String, Integer, text, Column
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
import asyncio

# 비동기 SQLite
DATABASE_URL = "sqlite+aiosqlite:///:memory:"

#엔진 생성(DB 이걸 사용하겠다고 알림)
engine = create_async_engine(
    DATABASE_URL,
    echo=True
)

# DB 세부 내용 세팅
## Base 클래스 생성 : python 에서 sql

class BaseModel(DeclarativeBase):
    pass

## 모델 정의 : DB에 들어갈 테이블 정의
class User(BaseModel):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True, index=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String)
    email: Mapped[str] = mapped_column(String, unique=True)

# DB 초기화 :

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(BaseModel.metadata.create_all)

# 데이터 베이스 세션 생성 : 연결 통로
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def get_db():
    async with AsyncSessionLocal() as session:
        yield session


# ===============================================
# CRUD


# 1. Create
async def create_user(name: str, email: str):
    async with AsyncSessionLocal() as db:
        new_user = User(name=name, email=email)
        db.add(new_user)
        await db.commit()
        await db.refresh(new_user)
        return new_user

# 2. Read
## 전체 사용자
async def get_all_users():
    async with AsyncSessionLocal() as db:
        result = await db.execute(text("SELECT * FROM users"))
        users = result.fetchall()
        return users

## 특정 사용자
async def get_user_by_email(email: str):
    async with AsyncSessionLocal() as db:
        result = await db.execute(text("SELECT * FROM users WHERE email = :email", email=email))
        user = result.fetchone()
        return user

# 3. Update
async def update_user(user_id: int, name: str, email: str):
    async with AsyncSessionLocal() as db:
        user = await db.get(User, user_id)
        if not user:
            return None
        user.name = name
        user.email = email
        await db.commit()
        await db.refresh(user)
        return user

# 4. Delete
async def delete_user(user_id: int):
    async with AsyncSessionLocal() as db:
        user = await db.get(User, user_id)
        if not user:
            return None
        await db.delete(user)
        await db.commit()
        return user_id


if __name__ == "__main__":
    async def main():
        await init_db()

        #사용자 생성
        create_user(name="", email="rlaalstjr2465@gmail.com")

    asyncio.run(main())