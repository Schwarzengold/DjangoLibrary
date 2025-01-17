from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, BookForm
from .models import Book
from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings
from django.contrib.auth.decorators import login_required
import os


def main(request):
    books = Book.objects.all()  
    return render(request, 'library/main.html', {'books': books})


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
