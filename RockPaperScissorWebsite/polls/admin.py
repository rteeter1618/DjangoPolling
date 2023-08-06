from django.contrib import admin
from .models import Question, Choice
# Register your models here.
#These objects will show up on the admin page
admin.site.register(Question)
admin.site.register(Choice)