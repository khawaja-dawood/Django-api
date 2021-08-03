from django.urls import path, include
from core.views import *
# from dj_rest_auth.views import LoginView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token


urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('', PostListCreateView.as_view(), name='get_create'),
    path('upde/<int:pk>/', PostUpdateDeleteView.as_view(), name='upd_del'),
    path('token/', obtain_jwt_token, name='get_token'),
    path('token/get/refresh/', refresh_jwt_token, name='refresh_token'),

    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('rest-auth/', include('rest_auth.urls')),

    # path('/dj-rest-auth/login/', LoginView),
    # path('api/token/', obtain_auth_token, name='obtain-token'),
]
