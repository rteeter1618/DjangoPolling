from django.utils import timezone
import datetime
from django.db import models

# Create your models here.

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField("Date published")

    #default way to display
    def __str__(self) -> str:
        return self.question_text
    
    def was_published_recently(self) -> bool:
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

class Choice(models.Model):
    #one to many, each choice has one question, questions have multiple choices
    #creates a choice_set field in Question instances
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    percent = models.FloatField(default=0)

    def __str__(self) -> str:
        return self.choice_text
    
    def setPercent(self, num):
        self.percent = num
