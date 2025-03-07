from django.contrib import admin
from django.urls import path, include
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    openapi.Info(
        title = "CRYAT API",
        default_version = "v1.0.0",
        description = "API doc for cryat",
    ),
    public = True,
)

urlpatterns = [
    path("api/v1/", include([
        path("healt-check/", HealthCheckView.as_view(), name = "health_check"),
        path("schema/", schema_view.with_ui("swagger", cache_timeout = 0), name = "swagger-schema"),
        path("admin/", admin.site.urls),
        ])),
]