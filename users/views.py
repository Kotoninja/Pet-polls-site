from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.hashers import make_password

User = get_user_model()


def login(request):
    if request.POST:
        user_username = request.POST["username"]
        user_password = request.POST["password"]
        return HttpResponse(f"{user_username},{user_password}")
    return render(request, "users/login.html", {})


def register(request):
    context = {}
    if request.POST:
        user_username = request.POST["username"]
        user_email = request.POST["email"]

        data = f"{user_username},{user_email},{request.POST['password']},{request.POST['repassword']}"

        # return HttpResponse(f"{User.objects.filter(email = user_email).exists()}")
        if request.POST["password"] != request.POST["repassword"]:
            return HttpResponse("repeat password is incorrect")
        elif User.objects.filter(email=user_email).exists():
            return HttpResponse("Аn account with this email address exists")
        else:
            return HttpResponse("user created")
    return render(request, "users/register.html",context=context)
