from django.urls import path

from . import views as v1

from rest_framework_simplejwt.views import (TokenObtainPairView, TokenRefreshView, TokenVerifyView)

urlpatterns = [
    path("login-by-login/", v1.Login.as_view(), name="login-by-login"),
    path("login-by-account/", v1.Login.as_view(), name="login-by-account"),
    path("registration/", v1.Registration.as_view(), name="registration"),
    path("authenticate/", v1.Authenticate.as_view(), name="authenticate"),
    path("authenticate/token/", TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path("authenticate/token/refresh/", TokenRefreshView.as_view(), name='token_refresh'),
    path("authenticate/token/verify/", TokenVerifyView.as_view(), name='token_verify'),
]