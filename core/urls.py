from django.urls import path, include
from core.views import *
# from dj_rest_auth.views import LoginView
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token

app_name = 'myCore'

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),

    path('', PostListCreateView.as_view(), name='get-posts'),
    path('upde/<int:pk>/', PostUpdateDeleteView.as_view(), name='upd-del'),
    path('books/', getBooksList.as_view(), name='get-books'),
    path('jwt/token/', obtain_jwt_token, name='get_token'),
    path('token/get/refresh/', refresh_jwt_token, name='refresh_token'),

    # path('dj-rest-auth/', include('dj_rest_auth.urls')),
    # path('rest-auth/', include('rest_auth.urls')),

    # path('/dj-rest-auth/login/', LoginView),
    # path('api/token/', obtain_auth_token, name='obtain-token'),
]
