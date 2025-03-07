from django.urls import path, re_path
from ../views/views.py import KafkaProxyView, HealthCheckView

urlpatterns = [
    re_path(r"^(?P<path>.*)$", KafkaProxyView.as_view()),
]
