from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import redirect
from contacts.models import Contact
# from django.core.mail import send_mail


def contacts(request):
    """render contact page"""

    if request.method == "POST":

        user = None
        if request.POST['user']:
            user = User.objects.get(username=request.POST['user'])

        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        user_email = request.POST['user_email']
        realtor_email = request.POST['realtor_email']
        phone = request.POST['phone']
        message = request.POST['message']

        # Check if user already submitted an inquery
        if request.user.is_authenticated:
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user=request.user
            )
        else:
            has_contacted = Contact.objects.all().filter(
                user_email=user_email, listing_id=listing_id
            )
        if has_contacted:
            messages.error(
                request, "you've already made an inquirey for this listing"
            )
            return redirect('/listings/'+listing_id)

        contact = Contact.objects.create(
            user=user, listing_id=listing_id, listing=listing, name=name,
            user_email=user_email, realtor_email=realtor_email,
            phone=phone, message=message
        )

        contact.save()

        # # Send Email to Realtor
        # send_mail(
        #     "Property Listing Inquiry",
        #     'There has been an Property Inquiry for "+listing+". \
        #         Sigin in for more info',
        #     "nuruddinsayeed22@gmail.com",
        #     [realtor_email, "nuruddinsayeed@gmail.com"],
        #     fail_silently=False
        # )

        messages.success(request,
                         "Your request has beed submited,\
                            arealtor will soon contact you")

        return redirect('/listings/'+listing_id)
