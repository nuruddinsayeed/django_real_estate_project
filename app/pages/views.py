

from django.http.response import HttpResponse


def index(request):
    """reders the index page"""

    return HttpResponse('<h1>Hello word</h>')
