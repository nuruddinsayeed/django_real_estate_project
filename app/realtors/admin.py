from django.contrib import admin
from .models import Realtor


class RealtorAdmin(admin.ModelAdmin):
    """Customize items display on realtor admin page"""

    ordering = ['id']
    list_display = ('id', 'name', 'email', 'hire_date',)
    list_display_links = ('id', 'name',)
    search_fields = ('name',)
    list_per_page = 25


#  register Realtor model with custom admin class
admin.site.register(Realtor, RealtorAdmin)
