from pydantic import BaseModel


class LoginResponse(BaseModel):
    message: str
    access_token: str
