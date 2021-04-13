from django.shortcuts import get_object_or_404, render
from .models import Listing
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.core.paginator import Paginator
from .choices import bedroom_choices, price_choices, state_choices


def index(request):
    """renders listing main page"""

    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)

    paginator = Paginator(listings, 3)
    page_number = request.GET.get('page')
    paged_listing = paginator.get_page(page_number)

    context = {
        "listings": paged_listing
    }

    return render(request, 'listings/index.html', context)


def listing(request, list_id):
    """renders single listing"""

    listing = get_object_or_404(Listing, pk=list_id)
    context = {
        "listing": listing
    }

    return render(request, 'listings/listing.html', context)


def search(request):
    """renders search page"""
    queryset_list = Listing.objects.order_by('-list_date')

    if 'keywords' in request.GET:
        keywords = request.GET['keywords']

        # Checking if its none
        if keywords:
            queryset_list = queryset_list.filter(
                description__icontains=keywords)

    if 'city' in request.GET:
        city = request.GET['city']

        # Checking if its none
        if city:
            queryset_list = queryset_list.filter(
                city__iexact=city)

    if 'state' in request.GET:
        state = request.GET['state']

        # Checking if its none
        if state:
            queryset_list = queryset_list.filter(
                state__iexact=state)

    if 'bedrooms' in request.GET:
        bedrooms = request.GET['bedrooms']

        # Here LTE(lte) means less then or equal
        if bedrooms:
            queryset_list = queryset_list.filter(
                bedrooms__lte=bedrooms)

    if 'price' in request.GET:
        price = request.GET['price']

        # Here LTE(lte) means less then or equal
        if price:
            queryset_list = queryset_list.filter(
                price__lte=price)

    context = {
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices,
        "listings": queryset_list,
        "values": request.GET
    }

    return render(request, 'listings/search.html', context)
