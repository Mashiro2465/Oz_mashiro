"""
메인 엔트리 (Main Entry)
- FastAPI 앱 생성 및 라우터 등록
- 앱 시작 시 DB 테이블 생성 및 시세 생성기 실행
"""
from argon2 import hash_password
from fastapi import FastAPI, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from jose import jwt
import asyncio

import models, auth, database
from routers import market, trade

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# market과 trade 라우터 등록
app.include_router(market.router)
app.include_router(trade.router)

@app.on_event("startup")
async def startup_event():
    """앱 시작 시 실행될 로직: DB 테이블 생성"""
    # 비동기 엔진을 사용하여 DB 테이블 생성
    async with database.engine.begin() as conn:
        await conn.run_sync(models.Base.metadata.create_all)

    # 시세 생성기(market.price_generator)를 백그라운드 태스크로 실행
    asyncio.create_task(market.price_generator())


@app.post("/register")
async def register(
    username: str, password: str, db: AsyncSession = Depends(database.get_db)
):
    """회원가입"""
    # TODO: 중복 아이디를 확인하고, 새로운 유저를 생성하여 DB에 저장하세요
    result = await db.execute(
        select(models.User).where(models.User.username == username)
    )
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail="중복된 아이디")

    new_user = models.User(
        username=username,
        password=auth.hash_password(password),
        balance=1000000
    )
    db.add(new_user)
    await db.commit()
    return {"msg" : f"{username}님 회원가입 성공"}

@app.post("/login")
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: AsyncSession = Depends(database.get_db),
):
    """로그인"""
    # TODO: 유저 정보를 확인하고, 비밀번호 검증 후 JWT 토큰을 발급하세요
    result = await db.execute(
        select(models.User).where(models.User.username == form_data.username)
    )
    user = result.scalar_one_or_none()

    if not user or auth.verify_password(form_data.password, user.password):
        raise HTTPException(status_code=401, detail="아이디 또는 비밀번호가 올바르지 않습니다.")

    access_token = auth.create_access_token({"username": user.username})
    return {"access_token": access_token, "token_type": "bearer"}

    # 토큰 만료 시간은 현재시간 + 15분 입니다.
    pass