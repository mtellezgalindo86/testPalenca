from fastapi import APIRouter
from app.adapters.profile.profile import AdaprterProfile
from app.domain.models.profile_response import MainProfileResponse
from app.use_cases.profile.profile import Profile

router = APIRouter()
external_services = AdaprterProfile()
profile = Profile(external_services)


@router.get("/uber/profile/{access_token}", response_model=MainProfileResponse)
def get_profile(access_token):
    return profile.get_profile(access_token)
