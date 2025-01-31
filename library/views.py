from django.shortcuts import render, get_object_or_404, redirect
from .models import Book, Author
from .forms import CustomUserCreationForm, BookForm, AuthorForm
from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os

def main(request):
    category_filter = request.GET.get('category', 'All')
    search_query = request.GET.get('search', '')
    categories = [
        "All", "Authors", "Fantasy", "Science Fiction", "Historical",
        "Adventure", "Mystery", "Romance", "Horror", "Biography", "Poetry", "Drama"
    ]
    if category_filter == "Authors":
        # Если выбрана категория "Authors", передаём в контекст список авторов
        authors = Author.objects.all()
        if search_query:
            authors = authors.filter(name__icontains=search_query)
        return render(request, 'library/main.html', {
            'authors': authors,
            'categories': categories,
            'category_filter': category_filter,
            'search_query': search_query,
        })
    else:
        books = Book.objects.all()
        if category_filter and category_filter != 'All':
            books = books.filter(category=category_filter)
        if search_query:
            books = books.filter(title__icontains=search_query)
        return render(request, 'library/main.html', {
            'books': books,
            'categories': categories,
            'category_filter': category_filter,
            'search_query': search_query,
        })

def author_list(request):
    """
    Отдельная страница для отображения списка авторов.
    Если нужна отдельная URL для авторів, можно использовать эту функцию.
    """
    search_query = request.GET.get('search', '')
    authors = Author.objects.all()
    if search_query:
        authors = authors.filter(name__icontains=search_query)
    categories = [
        "All", "Authors", "Fantasy", "Science Fiction", "Historical",
        "Adventure", "Mystery", "Romance", "Horror", "Biography", "Poetry", "Drama"
    ]
    return render(request, 'library/author_list.html', {
        'authors': authors,
        'categories': categories,
        'category_filter': "Authors",
        'search_query': search_query,
    })


def serve_pdf(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), content_type='application/pdf')
    else:
        return HttpResponseNotFound("The requested file was not found.")

def register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.email = form.cleaned_data['email']
            user.save()
            login(request, user)
            return redirect('main')
    else:
        form = CustomUserCreationForm()
    return render(request, 'library/register.html', {'form': form})

def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, 'library/book_detail.html', {'book': book})

def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = BookForm()
    return render(request, 'library/add_book.html', {'form': form})

@login_required
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('main')
    return render(request, 'library/confirm_delete.html', {'book': book})

def edit_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = BookForm(instance=book)
    return render(request, 'library/edit_book.html', {'form': form, 'book': book})

def author_detail(request, pk):
    author = get_object_or_404(Author, pk=pk)
    return render(request, 'library/author_detail.html', {'author': author})

def add_author(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AuthorForm()
    return render(request, 'library/add_author.html', {'form': form})

def edit_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        form = AuthorForm(request.POST, request.FILES, instance=author)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = AuthorForm(instance=author)
    return render(request, 'library/edit_author.html', {'form': form, 'author': author})

def delete_author(request, pk):
    author = get_object_or_404(Author, pk=pk)
    if request.method == 'POST':
        author.delete()
        return redirect('main')
    return render(request, 'library/delete_author.html', {'author': author})
