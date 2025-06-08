from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader

def index(request):
    return render(request, 'polls/home_page.html')
    # return HttpResponse(template.render({},request))