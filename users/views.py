from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib import messages


def login(request):
    return render(request,"users/login.html",{})


def register(request):
    return render(request,"users/register.html")