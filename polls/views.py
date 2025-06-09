from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader

from .models import Question


def index(request):
    context = {"all_quetions": Question.objects.all()}
    return render(request, "polls/home_page.html", context=context)

def question_window(request,question_id):
    question = {'question': get_object_or_404(Question, pk = question_id)}
    return render(request,"polls/question_page.html",context=question)
    # return HttpResponse(question)
    
def create_question(request):
    return HttpResponse('Question Constructor')