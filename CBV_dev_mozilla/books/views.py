from django.views.generic import ListView

from .models import Book


class BooksViewList(ListView):
    model = Book
    template = 'book_list.html'
    context_object_name = 'list_book'
