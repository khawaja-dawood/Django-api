from django.urls import path, include
from .views import AuthAPIView


urlpatterns = [
    path('', AuthAPIView.as_view())


]