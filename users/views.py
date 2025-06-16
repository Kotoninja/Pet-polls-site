from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
User = get_user_model()


def user_login(request):
    context = {}
    if request.POST:
        user_username = request.POST["username"]

        user = authenticate(request,username=user_username, password=request.POST["password"])
        if user is not None:
            login(request,user)
            return redirect('polls:home')
        else:
            context["error"] = "Invalid username or password entered"

    return render(request, "users/login.html", context=context)


def user_register(request):
    context = {}
    if request.POST:
        user_username = request.POST["username"]
        user_email = request.POST["email"]

        data = f"{user_username},{user_email},{request.POST['password']},{request.POST['repassword']}"

        if request.POST["password"] != request.POST["repassword"]:
            context["error"] = "Repeat password is incorrect"
        elif User.objects.filter(email=user_email).exists():
            context["error"] = "Аn account with this email address exists"
        else:
            user = User.objects.create_user(
                username=user_username,
                email=user_email,
                password=request.POST["password"],
            )
            return redirect("users:login")
    return render(request, "users/register.html", context=context)

@login_required
def user_progile(request):
    # logout(request)
   return HttpResponse(f"{request.user.username}, {request.user.date_joined}")