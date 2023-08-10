from django.urls import path

from . import views

#namespacing to make easier to access specifics
app_name = "polls"
urlpatterns = [
    # ex: /polls/
    path("", views.index, name="index"),
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # polls/allResults/
    path("allResults/", views.allResults, name="allResults"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
    # polls/addQuestion
    path("addQuestion/", views.addQuestion, name="addQuestion"),
    # polls/addQuestionUpdater
    path("addQuestionUpdater", views.addQuestionUpdater, name="addQuestionUpdater")
]