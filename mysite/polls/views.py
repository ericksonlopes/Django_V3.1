from django.http import HttpResponse


# views
def index(request):
    # Retorna str, como response
    return HttpResponse("Hello, world. You're at the polls index.")
