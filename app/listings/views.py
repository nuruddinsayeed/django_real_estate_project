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

    context = {
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices
    }

    return render(request, 'listings/search.html', context)
