from django.contrib import admin
from .models import Contact


class ContactAdmin(admin.ModelAdmin):
    """Customize Admin page components for Contacts"""

    list_display = ('id', 'name', 'user_email', 'listing', 'contact_date')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'listing', 'user_email')
    list_filter = ('listing',)
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
