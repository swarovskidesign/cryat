from django.urls import path, re_path
from .views.views import MyDefaultAPIView

urlpatterns = [
    path("lya/", MyDefaultAPIView.as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
    # path("", .as_view(), name=""),
]
