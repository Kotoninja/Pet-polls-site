from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from .models import Question


def index(request):
    print()
    context = {"all_quetions": Question.objects.all()}
    return render(request, "polls/home_page.html", context=context)


def question_window(request, question_id):
    """
    For tests
    1. Check if there is any choice
    2. Chechk if there is NO choice
    """
    print()
    if request.method == "POST":
        if request.POST.get("delete"):
            Question.objects.get(pk=question_id).delete()
            return HttpResponseRedirect(reverse("polls:home"))

    question = {"question": get_object_or_404(Question, pk=question_id)}
    return render(request, "polls/question_page.html", context=question)


def create_question(request):
    print()
    if request.method == "POST":
        question = request.POST.get("question")
        choices = request.POST.getlist("choices")

        new_question = Question.objects.create(question_text=question)

        print(choices)
        for choice in choices:
            if choice:
                new_question.choice_set.create(
                    choice_text=choice,
                )

        new_question.save()

        return HttpResponseRedirect(reverse("polls:question", args=(new_question.id,)))

    return render(request, "polls/create_question.html", context={})
