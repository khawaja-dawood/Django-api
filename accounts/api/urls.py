from django.urls import path, include
from .views import AuthAPIView, RegisterAPIView


urlpatterns = [
    path('', AuthAPIView.as_view()),
    path('register/', RegisterAPIView.as_view()),
]