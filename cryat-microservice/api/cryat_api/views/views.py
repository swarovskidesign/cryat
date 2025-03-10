from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

class MyDefaultAPIView(APIView):
    """
    Простой API, который возвращает JSON-ответ.
    """
    def get(self, request):
        # Ваши данные, которые вы хотите вернуть в JSON
        data = {
            "message": "Hello, World!",
            "status": "success",
            "data": {
                "item1": "value1",
                "item2": "value2",
            }
        }
        # Возвращаем ответ в формате JSON
        return Response(data, status=status.HTTP_200_OK)
