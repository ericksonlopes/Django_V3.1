from django.http import HttpResponse


# views
# def index(request):
#     # Retorna str, como response
#     return HttpResponse("Hello, world. You're at the polls index.")
from .models import Question


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request, question_id):
    return HttpResponse(f"You're looking at question {question_id}")


def results(request, question_id):
    return HttpResponse(f"You're looking at the results of questions. {question_id}")


def vote(request, question_id):
    return HttpResponse(f"You're voting on question {question_id}")
