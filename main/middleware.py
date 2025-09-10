from django.http import HttpResponseForbidden
from django.conf import settings

class AllowIframeOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith(settings.STATIC_URL):
            return self.get_response(request)

        allowed_referer = 'https://nmimsindore.acm.org'

        referer = request.META.get('HTTP_REFERER')

        if referer and referer.startswith(allowed_referer):
            return self.get_response(request)

        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Direct access is not allowed.</p>")