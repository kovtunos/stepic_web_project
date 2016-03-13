from django.contrib import admin
from .models import Question, Answer


class QuestionAdmin(admin.ModelAdmin):
    list_display = ('title', 'text', 'added_at', 'rating', 'author', 'likes')
    date_hierarchy = 'added_at'


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'added_at', 'author')
    date_hierarchy = 'added_at'
    raw_id_fields = ('question',)


admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer, AnswerAdmin)
