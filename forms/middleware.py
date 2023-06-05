from django.shortcuts import redirect
from django.urls import reverse


class RedirectAuthenticatedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.path in [reverse('login'), reverse('register')]:
            return redirect('home')  # Redirect to the home page if already authenticated

        response = self.get_response(request)
        return response
