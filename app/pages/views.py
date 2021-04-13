from django.shortcuts import render
from realtors.models import Realtor
from listings.models import Listing
from listings.choices import bedroom_choices, price_choices, state_choices


def index(request):
    """reders the index page"""

    listings = Listing.objects.all().order_by(
        '-list_date').filter(is_published=True)[:3]

    context = {
        "listings": listings,
        "price_choices": price_choices,
        "bedroom_choices": bedroom_choices,
        "state_choices": state_choices
    }
    return render(request, "pages/index.html", context)


def about(request):
    """renders the About page"""

    realtors = Realtor.objects.all().order_by('-hire_date')
    mvp_realtors = Realtor.objects.all().filter(is_mvp=True)

    context = {
        "realtors": realtors,
        "mvp_realtors": mvp_realtors
    }

    return render(request, "pages/about.html", context)
