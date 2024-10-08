from django.contrib import admin
from polls.models import Question, Choice

class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 1

class QuestionAdmin(admin.ModelAdmin):
    fields = ["pub_date", "question_text"]
    list_display = ("question_text", "pub_date",)
    list_display_links = ("pub_date",)
    list_filter=("pub_date",)
    date_hierarchy = "pub_date"
    inlines = [ChoiceInline]

class ChoiceAdmin(admin.ModelAdmin):
    list_display = ("question", "choice_text", "votes",)
    list_per_page = 1
    # list_max_show_all = 1
    list_editable = ("votes",)
    search_fields=("question__question_text", "choice_text", "votes")
    search_help_text="Search your Query Here"



admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice, ChoiceAdmin)
