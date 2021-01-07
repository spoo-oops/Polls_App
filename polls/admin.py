from django.contrib import admin

# Make poll app modifiable in admin
# Tells admin that Question obects have admin interface
from .models import Question
from .models import Choice
# Register your models here.
admin.site.register(Question)
admin.site.register(Choice)
