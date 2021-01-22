from django.contrib import admin

# Make poll app modifiable in admin
# Tells admin that Question obects have admin interface
from .models import Question
from .models import Choice
from .models import Category
# Register your models here.


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3

class QuestionInline(admin.TabularInline):
    model = Question


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    #for the main question page
    list_display = ('question_text', 'pub_date','category', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']

class CategoryAdmin(admin.ModelAdmin):
    model = Category
    inlines = [
        QuestionInline,
    ]
admin.site.register(Question, QuestionAdmin)
admin.site.register(Category, CategoryAdmin)

admin.site.register(Choice)
