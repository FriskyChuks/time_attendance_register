from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.hashers import make_password
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist

from django.contrib.auth.models import User
from .models import *

def login_view(request):
    msg = ""
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            msg = 'Invalid credentials'
            return render(request, "accounts/login.html", {"msg": msg})

    return render(request, "accounts/login.html", {"msg": msg})


def register_user(request):
    msg = ""
    registered_user = None
    if request.method == "POST":
        email = request.POST.get("email")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        check_user = User.objects.filter(email=email)
        print(check_user)
        if len(check_user) > 0:
            msg = 'This Email has already been used'
            return render(request, "accounts/register.html", {"msg": msg,})
        if password == confirm_password:
            user = User.objects.create_user(
                username=email, password=password, email=email)
            user.set_password(password)
            user = authenticate(username=email, password=password)
            login(request,user)
            return redirect('home')
        else:
            msg = 'Passwords do not match'
            return render(request, "accounts/register.html", {"msg": msg,})
    return render(request, "accounts/register.html", {"msg": msg,})



def logout_view(request):
    logout(request)
    return redirect('auth_login')


def profile_view(request):
    user_image = UserImage.objects.get(user_id=request.user.id)
    return render(request, 'accounts/profile.html', {'user_image':user_image})


def upload_image_view(request):
    msg = ''
    if request.method == 'POST':
        image = request.FILES.get('image')
        user_image = UserImage.objects.filter(user_id=request.user.id)
        if user_image:
            UserImage.objects.filter(user_id=request.user.id).update(image=image)
            msg = 'Image updated successfully'
        else:
            UserImage.objects.create(user=request.user, image=image)
            msg = 'Image uploaded successfully'
    
    return render(request, 'accounts/image.html',{'msg':msg})
