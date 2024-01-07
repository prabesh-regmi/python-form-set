# views.py

from django.shortcuts import render, redirect
from .forms import AuthorForm, BookFormSet

def create_author_with_books(request):
    if request.method == 'POST':
        author_form = AuthorForm(request.POST, prefix='author')
        book_formset = BookFormSet(request.POST, prefix='book')

        if author_form.is_valid() and book_formset.is_valid():
            author = author_form.save()
            books = book_formset.save(commit=False)

            for book in books:
                book.author = author
                book.save()

            return redirect('/')  # Redirect to a page displaying a list of authors
    else:
        author_form = AuthorForm(prefix='author')
        book_formset = BookFormSet(prefix='book')

    return render(request, 'create_author_with_books.html', {'author_form': author_form, 'book_formset': book_formset})
