from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Book, BookIssue
from datetime import date

def login_view(request):
    if request.method == 'POST':
        user = authenticate(request,
            username=request.POST['username'],
            password=request.POST['password'])
        if user:
            login(request, user)
            return redirect('dashboard')
    return render(request, 'login.html')

@login_required
def dashboard(request):
    return render(request, 'dashboard.html')

@login_required
def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

@login_required
def issue_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if book.available:
        BookIssue.objects.create(user=request.user, book=book)
        book.available = False
        book.save()
    return redirect('book_list')

def logout_view(request):
    logout(request)
    return redirect('login')
