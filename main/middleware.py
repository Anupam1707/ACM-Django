from django.http import HttpResponseForbidden
import os

class AllowIframeOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if any(segment in request.path for segment in ["static", "media"]):
            return self.get_response(request)

        allowed_referers = ['https://nmimsindore.acm.org', 'https://acm-django.onrender.com', 'http://127.0.0.1:8000/']
        referer = request.META.get('HTTP_REFERER')
        print("Referer:", referer)

        if referer:
            for allowed_referer in allowed_referers:
                if referer.startswith(allowed_referer) or referer == allowed_referer:
                    return self.get_response(request)

        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Direct access is not allowed.</p>")
