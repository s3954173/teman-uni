from django.contrib.auth.backends import BaseBackend
from temanuni.models import User as tmUser
from django.contrib.auth.hashers import check_password


class TemanUniLogin(BaseBackend):
    def authenticate(self, request, email=None, password=None, **kwargs):
        try:
            user = tmUser.objects.using('temanuni').get(email=email)
            user_id = user.user_id
            hashed_password_from_database = user.password
            if check_password(password, hashed_password_from_database):
                return user  # Return the user object
            return None
        except tmUser.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return tmUser.objects.using('temanuni').get(pk=user_id)
        except tmUser.DoesNotExist:
            return None
    