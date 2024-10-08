from django.shortcuts import render, HttpResponse, get_object_or_404, redirect
from polls.models import Question, Choice
from django.http import Http404, JsonResponse
from django.db.models import F


# Create your views here.
def index(request):
    latest_question_list = Question.objects.order_by("-pub_date")
    context = {
        "latest_question_list": latest_question_list,
    }
    return render(request, "index.html", context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "detail.html", {"question": question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, "results.html", {"question": question})


def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST.get("choice", False):
        selected_choice = question.choice_set.get(pk=request.POST.get("choice"))
        selected_choice.votes += 1
        selected_choice.save()
        return redirect("polls:results", question.id)
    else:
        return render(
            request,
            "detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )

def vote_api(request, question_id):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        return JsonResponse({"error": "Question Doesn't exists"})

    if request.POST.get("choice", False):
        selected_choice = question.choice_set.get(pk=request.POST.get("choice"))
        selected_choice.votes += 1
        selected_choice.save()
        return JsonResponse({"success": True})
    else:
        return JsonResponse(
            {
                "error": "You didn't select a choice.",
            },
        )
