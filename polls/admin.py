from django.contrib import admin
from .models import Question, Choice

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'pub_date')
    list_display_links = ('question_text',)
    list_filter = ('question_text',)
    search_fields = ['question']
    date_hierarchy = 'pub_date'
    ordering = ['pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_display_links = ('choice_text',)
    list_filter = ('question', 'choice_text')
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
