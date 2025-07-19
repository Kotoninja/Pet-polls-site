from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import UserInfo
from polls.models import Question

User = get_user_model()


def user_login(request):
    context = {}
    if request.POST:
        user_username = request.POST["username"]

        user = authenticate(
            request, username=user_username, password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return redirect("polls:home")
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

            UserInfo.objects.create(user=user)

            return redirect("users:login")
    return render(request, "users/register.html", context=context)


@login_required
def user_profile(request, profile_nickname):
    """
    TODO Photo editing system (until to 20th Jul)
    """
    try:
        user = User.objects.get(username=profile_nickname)

        context = {
            "user": user,
            "count_created_of_polls": UserInfo.objects.get(
                user=user
            ).count_created_of_polls,
            "count_answered_of_polls": UserInfo.objects.get(
                user=user
            ).count_answered_of_polls,
            "question_list": Question.objects.filter(question_author=user.username),
        }

    except User.DoesNotExist:
        raise Http404

    if request.method == "POST":
        if request.POST.get("logout", False):
            logout(request)
            return redirect("polls:home")
    return render(request, "users/profile.html", context=context)
