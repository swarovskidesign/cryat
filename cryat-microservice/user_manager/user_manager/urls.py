from .documentation import schema_view

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("api/", include([
        path("v1/", include("manager.urls")),
        path("schema/", schema_view.with_ui("swagger", cache_timeout = 0), name = "swagger-schema"),
        path("admin/", admin.site.urls),
    ])),
]