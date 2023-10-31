from app.adapters.profile.profile import AdaprterProfile


class Profile:
    def __init__(self, external_service: AdaprterProfile):
        self.external_service = external_service

    def get_profile(self, token):
        return self.external_service.get_profile(token)
