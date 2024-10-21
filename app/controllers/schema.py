from pydantic import BaseModel


class UpdateEmailRequest(BaseModel):
    email: str


class UpdatePhoneRequest(BaseModel):
    phone: str


class UpdatePasswordRequest(BaseModel):
    old_password: str
    new_password: str
