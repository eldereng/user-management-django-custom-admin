from django.contrib import admin
from django.urls import path, include

from people.views import SignUpView
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('/', include('people.urls')),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('api-token-auth/', obtain_auth_token, name='api_token_path'),
]
