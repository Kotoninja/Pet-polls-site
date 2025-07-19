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
from .models import Question, Tag
from users.models import UserInfo


def solr_status_code(
    core: str, url: str = "http://127.0.0.1:8983/solr", timeout: int = 10
):
    try:
        solr = pysolr.Solr(url=f"{url}/{core}", timeout=timeout)
        ping = solr.ping()
        return 1
    except pysolr.SolrError:
        return 0


def home(request):
    context: dict = {
        "all_questions": Question.objects.all(),
    }

    if request.method == "GET":
        if request.GET.get("search"):
            response: str = request.GET.get("search")
            context["search_value"] = response

            if solr_status_code(
                core="polls"
            ):  # If solr server is work - use solr search, else use deafult search
                print("solr search")
                results = (
                    SearchQuerySet()
                    .models(Question)
                    .filter(content=response)
                    .load_all()
                )

                context["all_questions"] = [result.object for result in results]
            else:
                print("default search")
                context["all_questions"] = Question.objects.filter(
                    question_text__icontains=response
                )

            if not context["all_questions"]:
                context["search_error"] = 1
    return render(request, "polls/home_page.html", context=context)


def question_page(request, question_id):
    context = {}

    question = get_object_or_404(Question, pk=question_id)

    context["question"] = question
    context["tags"] = question.tags.all()
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
            if created_polls.count_created_of_polls > 0:
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
        tags = request.POST.getlist("tags")
        choices = request.POST.getlist("choices")

        new_question: Question = Question.objects.create(
            question_author=creator, question_text=question
        )

        for tag in tags:
            if Tag.objects.filter(tag_text=tag).exists():
                tag = Tag.objects.get(tag_text=tag)
            else:
                tag = Tag.objects.create(tag_text=tag)
                tag.save()
            new_question.tags.add(tag)

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

        return HttpResponseRedirect(reverse("polls:question", args=(new_question.pk,)))

    return render(request, "polls/create_question.html", context=context)
