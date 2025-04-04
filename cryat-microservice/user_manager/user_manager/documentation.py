from drf_yasg import openapi
from drf_yasg.views import get_schema_view

from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title = "CRYAT user manager",
        default_version = "v1.0.0",
        description = "doc for cryat",
    ),
    public = True,
    permission_classes=(permissions.AllowAny,),
)