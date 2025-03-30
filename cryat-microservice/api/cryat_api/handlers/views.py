from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError

from .. import serializers
from ..models.models import Token_users


class Authenticate(CreateAPIView):
    """
    Универсальная аутентификация (по логину или номеру счета)
    """
    queryset = Token_users.objects.all()

    def get_serializer_class(self):
        # Определяем, какой сериализатор использовать
        data = self.request.data
        if "username" in data:
            return serializers.UserSerializerNickname
        elif "account_number" in data:
            return serializers.UserSerializerAccount
        else:
            raise ValidationError({"detail": "You must specify all the data"})

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({"token": user.auth_token.key}, status=status.HTTP_200_OK)