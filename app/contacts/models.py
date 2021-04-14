from datetime import datetime
from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    """Create Database model for clients inquiry"""

    user = models.ForeignKey(User, blank=True, null=True,
                             on_delete=models.DO_NOTHING)

    listing_id = models.CharField(max_length=255)
    listing = models.CharField(max_length=255)
    name = models.CharField(max_length=100)
    realtor_email = models.CharField(max_length=100)
    user_email = models.CharField(max_length=100)
    phone = models.CharField(max_length=50)
    message = models.TextField(blank=True)
    contact_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return self.name
