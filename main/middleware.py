# main/middleware.py

from django.http import HttpResponseForbidden

class AllowIframeOnlyMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        # This is the allowed domain that can embed your site.
        allowed_referer = 'https://nmimsindore.acm.org'

        # Get the Referer header from the request.
        referer = request.META.get('HTTP_REFERER')

        # Allow access if the referer is the allowed one.
        # The 'startswith' check allows any page on that domain.
        if referer and referer.startswith(allowed_referer):
            return self.get_response(request)

        # Block access for all other cases (including direct access).
        return HttpResponseForbidden("<h1>403 Forbidden</h1><p>Direct access is not allowed.</p>")