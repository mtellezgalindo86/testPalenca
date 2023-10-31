from fastapi import HTTPException

from app.domain.entities.user import User
from app.config.constans import VALID_CREDENTIALS


class AdapterLogin:
    @staticmethod
    def login(user: User):
        if (
            user.email == VALID_CREDENTIALS["email"]
            and user.password == VALID_CREDENTIALS["password"]
        ):
            return {"message": "SUCCESS", "access_token": VALID_CREDENTIALS["access_token"]}

        raise HTTPException(status_code=401, detail={"message": "Credentials Invalids",
                                                     "details": "Incorrect access token"})
