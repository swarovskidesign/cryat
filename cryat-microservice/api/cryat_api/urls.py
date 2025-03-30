from .handlers import views
from django.urls import re_path, path


urlpatterns = [
    # path("create-token/", views.CreateTokenView.as_view(), name="create-token"),
    # path("get-token/", views.GetTokenView.as_view(), name="get-token"),
    path("authenticate-by-login", views.Authenticate.as_view(), name="authenticate-by-login"),
    path("authenticate-by-account", views.Authenticate.as_view(), name="authenticate-by-account")
]