from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.status import HTTP_200_OK


class AllAllowedHostsHealthCheckerMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path == "/api/v1/health/":
            return JsonResponse({"message": "Health OK."}, status=HTTP_200_OK)
