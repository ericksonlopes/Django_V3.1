from django.contrib import admin

from .models import Question, Choice

# Registrando aplicação dentro do admin
admin.site.register(Question)
admin.site.register(Choice)
