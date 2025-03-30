from rest_framework import serializers

class UserSerializerNickname(serializers.Serializer):
    """
    Сериализатор по никнейму
    """
    class Meta:
        fields = ["username", "password"]

class UserSerializerAccount(serializers.Serializer):
    """
    Сериализатор по номеру счета
    """
    class Meta:
        fields = ["account_number", "password"]

class UserSerializer(serializers.Serializer):
    """
    Сериализатор по логину и паролю
    """
    class Meta:
        fields = ["username", "password"]