from django.shortcuts import render


def index(request):
    """renders listing main page"""

    return render(request, 'listings/index.html')


def listing(request):
    """renders single listing"""

    return render(request, 'listings/listing.html')


def search(request):
    """renders search page"""

    return render(request, 'listings/search.html')
