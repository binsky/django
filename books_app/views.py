from django.shortcuts import render
from books_app.models import Book, Publisher, Author


def search_book(request):
    return render(request, 'booksapp/books.html', {'current_section' : 'Search book'})


def book_res(request):
    title = request.GET.get("title", "")
    publisher = request.GET.get("publisher", "")
    afname = request.GET.get("first_name", "")
    alname = request.GET.get("last_name", "")
    books = Book.objects.filter(title__icontains=title, authors__first_name__istartswith=afname,
                                authors__last_name__istartswith=alname, publisher__name__icontains=publisher)
    return render(request, 'booksapp/books_found.html', {'current_section': 'Search result', 'books': books})

