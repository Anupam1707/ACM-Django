from django.http import HttpResponseForbidden
from django.conf import settings
class AllowIframeOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if settings.DEBUG:
            return self.get_response(request)

        if request.path.startswith(settings.STATIC_URL) or request.path.startswith(settings.MEDIA_URL):
            return self.get_response(request)

        elif request.path.startswith('/admin/'):
            return self.get_response(request)

        allowed_referers = ['https://nmimsindore.acm.org', 'https://acm-django.onrender.com']
        referer = request.META.get('HTTP_REFERER')

        if referer:
            for allowed_referer in allowed_referers:
                if referer.startswith(allowed_referer):
                    return self.get_response(request)

        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Direct access is not allowed.</p>")