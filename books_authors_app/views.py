from django.shortcuts import render, redirect
from books_authors_app.models import Book, Author

def index(request):
    context = {
        "all_books": Book.objects.all()
    }
    return render(request, 'index.html', context)

def crear_libro(request):
    Book.objects.create(title=request.POST['title'], desc=request.POST['desc'])
    return redirect('/')

def ver_libro(request, id):
    context = {
        "all_authors": Author.objects.all(),
        "book": Book.objects.get(id=id)
    }
    return render(request, 'ver_libro.html', context)

def agregar_autor(request, id):
    the_book = Book.objects.get(id=id)
    print("-"*20, the_book)
    selected_author = Author.objects.get(id=request.POST['author_id'])
    print("-"*20, selected_author)
    the_book.authors.add(selected_author)
    return redirect(f'/books/{id}')

def index_authors(request):
    context = {
        "all_authors": Author.objects.all()
    }
    return render(request, 'authors.html', context)

def crear_autor(request):
    Author.objects.create(last_name=request.POST['last_name'], first_name=request.POST['first_name'], notes=request.POST['notes'])
    return redirect('/authors')

def ver_autor(request, id):
    context = {
        "all_books": Book.objects.all(),
        "author": Author.objects.get(id=id)
    }
    return render(request, 'ver_autor.html', context)

def agregar_libro(request, id):
    the_author = Author.objects.get(id=id)
    selected_book = Book.objects.get(id=request.POST['book_id'])
    the_author.books.add(selected_book)
    return redirect(f'/authors/{id}')