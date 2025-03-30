# from api.api.config import MICROSERVICE_str

# import requests

# from rest_framework import status
# from rest_framework.request import Request
# from rest_framework.response import Response

# from ..utils import get_uri_for_proxy

# class ProxyingToMicroservices:

#     def proxy(self, request: Request):
#         try:
#             uri = get_uri_for_proxy(request.build_absolute_uri())
#             target_url = MICROSERVICE_str[uri]
#             method = request.method.lower()
#             data = request.data
#             headers = request.headers

#             response = getattr(requests, method)(target_url, json=data, headers=headers)
#             return Response(response.json(), status=response.status_code)

#         except requests.exceptions.ProxyError:
#             return Response({"error_connections": "our service unavailable"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except requests.exceptions.ConnectionError:
#             return Response({"error_connections": "our service unavailable"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except requests.exceptions.RequestException as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         except Exception as e:
#             return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        