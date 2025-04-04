from django.urls import path

from ..handlers import views as v1

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("login-by-username/", v1.Login.as_view(), name="login-by-username"),
    path("login-by-account/", v1.Login.as_view(), name="login-by-account"),
    path("registration/", v1.Registration.as_view(), name="registration"),
    path("authenticate/token/", TokenObtainPairView.as_view(), name='token-obtain'),
    path("authenticate/token/refresh/", TokenRefreshView.as_view(), name='token-refresh'),
    path("authenticate/token/verify/", TokenVerifyView.as_view(), name='token-verify'),
]