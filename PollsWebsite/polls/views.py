from django.shortcuts import get_object_or_404, render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

from polls.models import Question, Choice


# Create your views here.
def index(request):
    from django.http import HttpResponse
from django.template import loader



def index(request):
    #gets the first 5 objects from the database
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    #Uses the html template string given, passing context so template can access
    #returns httpresponse with that template
    return render(request, "polls/index.html", context)

#question_id given in get(url)
def detail(request, question_id):
    #gets question from database or errors
    question = get_object_or_404(Question, pk=question_id)

    return render(request, "polls/detail.html", {"question": question})


def results(request, question_id):

    question = get_object_or_404(Question, pk=question_id)
    totalNum = 0
    for choice in question.choice_set.all():
        totalNum+=choice.votes
    
    for choice in question.choice_set.all():
        choice.percent = F("votes") * 100 / totalNum
        choice.save()

    return render(request, "polls/results.html", {"question" : question})


def vote(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    try:
        #request.POST is a dictionary of info, always returns strings
        #the key "choice" is from the choice name in <input... in detail.html
        #can do the same for GET, the form sent data through post in this case
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.doesNotExist):
        # Redisplay the question voting form.
        return render(
            request,
            "polls/detail.html",
            {
                "question": question,
                "error_message": "You didn't select a choice.",
            },
        )
    else:
        selected_choice.votes = F("votes") + 1
        selected_choice.save()
    #return HttpResponseRedirect after dealing with post data, so that it is not double updated if user hits back
    #redirects to given url, reverse constructs that url using urls.py
    return HttpResponseRedirect(reverse("polls:results", args=(question.id,)))