from django.urls import path, include
from .views import AuthAPIView, RegisterAPIView

urlpatterns = [

    # api endpoint for data get without signing in, anyone can access this authenticated or unauthenticated users
    path('api/get/', AuthAPIView.as_view(), name='login'),

    # registering a user using useranme, email ,password and password2
    path('api/register/', RegisterAPIView.as_view()),

    path('api/users/', include('accounts.api.user.urls'))
]
