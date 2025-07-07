from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.decorators import login_required
import json

# apps models
from .models import Question
from users.models import UserInfo


def index(request):
    context = {"all_quetions": Question.objects.all()}
    return render(request, "polls/home_page.html", context=context)


def question_window(request, question_id):
    if request.method == "POST":
        if request.POST.get(
            "delete"
        ):  # TODO in case delete question, the counter of created polls need decrease
            Question.objects.get(pk=question_id).delete()
            return HttpResponseRedirect(reverse("polls:home"))

        elif request.POST.get("choice"):
            udpate_the_user_ans_filed = UserInfo.objects.get(user=request.user)
            udpate_the_user_ans_filed.count_answered_of_polls = (
                F("count_answered_of_polls") + 1
            )
            udpate_the_user_ans_filed.save()

            question = Question.objects.get(pk=question_id)
            choice = question.choice_set.get(pk=request.POST.get("choice"))  # type: ignore

            question.question_votes = F("question_votes") + 1
            question.save()
            choice.choice_votes = F("choice_votes") + 1
            choice.save()

            return HttpResponseRedirect(
                reverse(
                    "polls:question",
                    args={
                        question_id,
                    },  # type: ignore
                )
            )

    question = {"question": get_object_or_404(Question, pk=question_id)}
    return render(request, "polls/question_page.html", context=question)


@login_required
def create_question(request):
    context = {}
    json_data = {'creator': request.user.username}
    context["json_data"] = json_data

    # print(context)
    if request.method == "POST":
        question = request.POST.get("question")
        choices = request.POST.getlist("choices")
        creator = request.POST.get("creator")

        print(creator)
        # new_question = Question.objects.create(question_text=question)

        # print(choices)
        # for choice in choices:
        #     if choice:
        #         new_question.choice_set.create(  # type: ignore
        #             choice_text=choice,
        #         )

        # new_question.save()

        # udpate_the_user_created_filed = UserInfo.objects.get(user=request.user)
        # udpate_the_user_created_filed.count_created_of_polls = (
        #     F("count_created_of_polls") + 1
        # )
        # udpate_the_user_created_filed.save()

        # return HttpResponseRedirect(reverse("polls:question", args=(new_question.id,)))

    return render(request, "polls/create_question.html", context=context)
