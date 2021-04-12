from django.contrib import admin
from .models import Listing


class ListingAdmin(admin.ModelAdmin):
    """Customize the items to display on listing admin page"""

    ordering = ['id']
    list_display = ('id', 'title', 'is_published',
                    'price', 'list_date', 'realtor',)
    list_display_links = ('id', 'title',)
    list_filter = ('realtor',)
    list_editable = ('is_published',)
    search_fields = ('title', 'adderss', 'city',
                     'state', 'zipcode', 'description', 'price')
    list_per_page = 25


# add listing wiht custom listing class to admin page
admin.site.register(Listing, ListingAdmin)
