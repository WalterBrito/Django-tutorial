from django.contrib import admin
from .models import Question, Choice

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionAdmin(admin.ModelAdmin):
    date_hierarchy = 'pub_date'
    fieldsets = [
        (None,                {'fields': ['question_text']}),
        ('Date information',  {'fields': ['pub_date']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('question_text', 'pub_date', 'was_published_recently')
    list_display_links = ('question_text',)
    list_filter = ['pub_date']
    search_fields = ['question_text']
    ordering = ['pub_date']

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ('question', 'choice_text', 'votes')
    list_display_links = ('choice_text',)
    list_filter = ('question', 'choice_text')
    search_fields = ['question']

admin.site.register(Question, QuestionAdmin)
# admin.site.register(Choice, ChoiceAdmin)
