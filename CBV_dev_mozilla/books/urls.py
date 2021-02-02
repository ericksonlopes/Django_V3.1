from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.BooksViewList.as_view(), name='list_book')
]
