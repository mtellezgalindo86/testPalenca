from pydantic import BaseModel


class ProfileResponse(BaseModel):
    country: str
    city_name: str
    worker_id: str
    first_name: str
    last_name: str
    email: str
    phone_prefix: str
    phone_number: str
    rating: str
    lifetime_trips: int


class MainProfileResponse(BaseModel):
    message: str
    platform: str
    profile: ProfileResponse
