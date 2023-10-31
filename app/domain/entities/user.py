from pydantic import BaseModel


class User(BaseModel):
    email: str.min_length=5
    password: str
