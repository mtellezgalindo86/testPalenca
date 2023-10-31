from fastapi import APIRouter
from app.adapters.login.login import AdapterLogin
from app.domain.entities.user import User
from app.domain.models.login_response import LoginResponse
from app.use_cases.login.login import Login

router = APIRouter()
external_services = AdapterLogin()
login_case = Login(external_services)


@router.post('/uber/login', response_model=LoginResponse)
def login(user: User):
    return login_case.login(user)
