# from rest_framework.views import APIView
# from rest_framework.generics import CreateAPIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.exceptions import ValidationError

# from ..models import serializers
# from ..models.models import Users

    
# class Registration(APIView):
#     """
#     Регистрация пользователя
#     """
#     permission_classes = [AllowAny]
#     serializer_class = serializers.RegistrationSerializer
    
#     def post(self, request):
#         serializer = serializers.RegistrationSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class Login(CreateAPIView):
#     """
#     Авторизация пользователя
#     """
#     queryset = Users.objects.all()
#     serializer_class = serializers.LoginSerializer
#     permission_classes = [AllowAny]
#     http_method_names = ['post']


# class Authenticate(CreateAPIView):
#     """
#     Универсальная аутентификация (по логину или номеру счета)
#     """
#     ...
    