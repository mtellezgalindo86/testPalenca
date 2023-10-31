from app.use_cases.login.login import Login
from app.adapters.login.login import AdapterLogin
from app.domain.entities.user import User


def test_login_success():
    external_services = AdapterLogin()
    login_case = Login(external_services)
    user = User(email="pierre@palenca.com", password="MyPwdChingon123")
    response = login_case.login(user)
    assert response["message"] == "SUCCESS"


def test_login_failure():
    external_services = AdapterLogin()
    login_case = Login(external_services)
    user = User(email="pierre@palenca.com", password="MyPwdChingon123")
    response = login_case.login(user)
    assert response["message"] == "SUCCESS"