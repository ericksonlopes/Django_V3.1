from django.contrib import admin

from .models import Question

# Registrando aplicação dentro do admin
admin.site.register(Question)
