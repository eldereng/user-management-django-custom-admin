from django.contrib import admin
from django.urls import path, include

from people.views import LoginView, UserCreate
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('people.urls')),
    path('users/', UserCreate.as_view(), name='user_create'),
    path("login/", LoginView.as_view(), name="login"),
    path('api-token-auth/', obtain_auth_token, name='api_token_path')
]
