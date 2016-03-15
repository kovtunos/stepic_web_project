from django.contrib import admin
from .models import Question, Answer
import pytz


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'added_at', 'author', 'rating')
    date_hierarchy = 'added_at'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'added_at', 'author')
    date_hierarchy = 'added_at'
    raw_id_fields = ('question',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
