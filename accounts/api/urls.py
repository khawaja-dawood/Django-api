from django.urls import path, include
from .views import AuthAPIView, RegisterAPIView
from accounts.api.user.views import UserDetailView, UserPostView

app_name = 'accounts'

urlpatterns = [

    # api endpoint for data get without signing in, anyone can access this authenticated or unauthenticated users
    path('token/', AuthAPIView.as_view(), name='login'),

    # registering a user using useranme, email ,password and password2
    path('register/', RegisterAPIView.as_view()),
    path('<str:username>/', UserDetailView.as_view(), name='detail'),
    path('<str:username>/posts/', UserPostView.as_view(), name='post-list'),

    # path('', include('accounts.api.user.urls'))
]
