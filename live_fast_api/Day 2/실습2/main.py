from datetime import datetime, timezone
from fastapi import FastAPI
from pydantic import BaseModel, Field, field_validator, EmailStr


class Reservatoins(BaseModel):
    name: str = Field(..., max_length=50, description="Reservatoin name은 최대 50자 까지 기입 가능합니다")
    email : EmailStr
    date : datetime
    sqecial_request : str =""

    @field_validator("date")
    @classmethod
    def date_validator(cls, value: datetime):
        now_utc = datetime.now(timezone.utc)

        if value < now_utc:
            raise ValueError("예약 날짜는 현재 시간 이후여야 합니다.")
        return value


app = FastAPI()

@app.post("/reservatoins/")
async def post_reservatoins(reservatoins: Reservatoins):
    return {"reservatoins": reservatoins}