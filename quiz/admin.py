from .models import Question, Category
from django.contrib import admin

class QuestionsAdmin(admin.ModelAdmin):
    list_display = ('question_de', 'get_tags', 'timestamp')
    list_filter = ['tags']
    search_fields = ['question_de', 'question_fr', 'question_it', 'question_en']
    filter_horizontal = ['tags']
    fieldsets = (
        ('Deutsch', {
            'fields': ('question_de', 'answer1_de', 'answer2_de', 'answer3_de')
        }),
        ('Francais', {
            'fields': ('question_fr', 'answer1_fr', 'answer2_fr', 'answer3_fr')
        }),
        ('Italiano', {
            'fields': ('question_it', 'answer1_it', 'answer2_it', 'answer3_it')
        }),
        ('English', {
            'fields': ('question_en', 'answer1_en', 'answer2_en', 'answer3_en')
        }),
        ('Tag', {
            'fields': ['tags']
        }),
    )

admin.site.register(Question, QuestionsAdmin)
