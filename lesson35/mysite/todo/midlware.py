from django.http import HttpResponse, HttpResponseRedirect


class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        if not request.user.is_authenticated and request.path == '/':
            return HttpResponseRedirect('login/')
        response = self.get_response(request)
        return response