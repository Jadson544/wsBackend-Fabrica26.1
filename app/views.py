from django.shortcuts import render, redirect
from .models import Book, Author, Category

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})

import requests

def characters(request):
    response = requests.get("https://rickandmortyapi.com/api/character")
    data = response.json()
    return render(request, 'characters.html', {'characters': data['results']})
