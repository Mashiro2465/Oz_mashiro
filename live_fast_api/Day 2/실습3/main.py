from fastapi import FastAPI
from pydantic import BaseModel, EmailStr, model_validator


class ContactInfo(BaseModel):
    email : EmailStr | None = None
    phone : str | None = None

    @model_validator(mode='after')
    def validate_contact_info(self):
        if (self.email or self.phone) is None:
            raise ValueError('둘중하나는 꼭 기입해 주세요')
        return self

app = FastAPI()

@app.post("/contact/")
async def create_contact(contact: ContactInfo):
    return {
        "msg": "Contact info accepted",
        "date" : contact
    }