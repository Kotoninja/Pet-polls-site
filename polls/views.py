# django
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from django.db.models import F
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

# other
from haystack.query import SearchQuerySet
import pysolr

# apps models
from .models import Question
from users.models import UserInfo


def home(request):
    """
    TODO Add hashtag (until the 15th Jul)
    FIXME Update search system, but url when user send a requests so big
    FIXME do right link
    """
    context = {
        "all_questions": Question.objects.all(),
        "search_value": "",
    }
    if request.method == "GET":
        if request.GET.get("search"):
            responese = request.GET.get("search")
            context["search_value"] = responese

            results = (
                SearchQuerySet()
                .models(Question)
                .filter(content=request.GET["search"])
                .load_all()
            )

            context["all_questions"] = [result.object for result in results]

    return render(request, "polls/home_page.html", context=context)


def question_page(request, question_id):
    context = {}

    question = get_object_or_404(Question, pk=question_id)

    context["question"] = question
    if question.question_author != "Anonymous":
        author = reverse(
            "users:profile", kwargs={"profile_nickname": question.question_author}
        )
        context["author"] = author

    if request.method == "POST":
        if request.POST.get("delete"):
            # Reducing count of created polls at user
            created_polls = UserInfo.objects.get(
                user=User.objects.get(username=question.question_author)
            )
            created_polls.count_created_of_polls = F("count_created_of_polls") - 1
            created_polls.save()

            # Delete question
            Question.objects.get(pk=question_id).delete()

            return HttpResponseRedirect(reverse("polls:home"))

        elif request.POST.get("choice"):
            # Add
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

    return render(request, "polls/question_page.html", context=context)


@login_required
def create_question(request):
    context = {}
    json_data = {"creator": request.user.username}
    context["json_data"] = json_data

    if request.method == "POST":
        creator = request.POST.get("creator")
        question = request.POST.get("question")
        choices = request.POST.getlist("choices")

        new_question: Question = Question.objects.create(
            question_author=creator, question_text=question
        )

        for choice in choices:
            if choice:
                new_question.choice_set.create(  # type: ignore
                    choice_text=choice,
                )

        new_question.save()

        if creator == request.user.username:
            udpate_the_user_created_filed = UserInfo.objects.get(user=request.user)
            udpate_the_user_created_filed.count_created_of_polls = (
                F("count_created_of_polls") + 1
            )
            udpate_the_user_created_filed.save()

        return HttpResponseRedirect(reverse("polls:question", args=(new_question.id,)))

    return render(request, "polls/create_question.html", context=context)
