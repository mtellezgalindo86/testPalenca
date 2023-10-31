from app.adapters.login.login import AdapterLogin


class Login:
    def __init__(self, external_service: AdapterLogin):
        self.external_service = external_service

    def login(self, user):
        return self.external_service.login(user)
