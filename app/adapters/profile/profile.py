from fastapi import HTTPException
from app.config.constans import PROFILE, VALID_CREDENTIALS


class AdaprterProfile:
    @staticmethod
    def get_profile(accessToken):
        if accessToken == VALID_CREDENTIALS['access_token']:
            return {"message": "SUCCESS", "platform": "uber", "profile": PROFILE}
        raise HTTPException(status_code=401, detail={"message": "Credentials Invalids",
                                                     "details": "Incorrect access token"})
