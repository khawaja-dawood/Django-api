import datetime
from django.conf import settings
from django.utils import timezone
# from rest_framework_jwt.settings import api_settings
# from core import mode

# expire_delta             = api_settings.defaults['JWT_REFRESH_EXPIRATION_DELTA']
expire_delta             = settings.JWT_AUTH['JWT_REFRESH_EXPIRATION_DELTA']
# print(expire_delta)



def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user': user.username,
        'expires': timezone.now() + expire_delta - datetime.timedelta(seconds=200)
    }