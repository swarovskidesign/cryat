from .documentation import schema_view

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/v1/", include([
        path("", include("cryat_api.urls")),
        path("schema/", schema_view.with_ui("swagger", cache_timeout = 0), name = "swagger-schema"),
        ])),
]