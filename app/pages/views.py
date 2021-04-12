from django.shortcuts import render


def index(request):
    """reders the index page"""

    return render(request, "pages/index.html", )


def about(request):
    """renders the About page"""

    return render(request, "pages/about.html",)
