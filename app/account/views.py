from django.shortcuts import redirect, render
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login, logout as auth_logout


def dashboard(request):
    """Renders user dashboard page"""

    return render(request, 'account/dashboard.html')

# its callde login so I change default logoin to auth_login


def login(request):
    """Renders Login page"""

    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            messages.success(request, "you are now logged in")
            return redirect('dashboard')
        else:
            messages.error(request, "invalid credetials")
            return redirect('login')
    else:
        return render(request, 'account/login.html')


def logout(request):
    """Redicrect to login with logged out"""

    if request.method == "POST":
        auth_logout(request)
        messages.success(request, "you are now logged out")
        return redirect('index')


def register(request):
    """Render user register page"""

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password']

        if password == password2:
            if User.objects.filter(username=username).exists():
                messages.error(request, "username already taken")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.error(request, "Email being used")
                return redirect(register)
            else:
                user = User.objects.create_user(
                    username=username,
                    email=email,
                    first_name=first_name,
                    last_name=last_name
                )
                user.save()
                # login(request, user)
                # messages.success(
                #     request, "successfully account created and logged in")
                # return redirect('index')
                messages.success(request, "Account Creation Succeeded")
                return redirect('login')
        else:
            messages.error(request, "Password did not mathc")
            return redirect('register')
    else:
        return render(request, 'account/register.html')
