from django.shortcuts import render, HttpResponse
from .models import book, author

def index(request):
    if request.method == "POST":
        book.objects.create(title=request.POST['titulo'],desc=request.POST['descripcion'])
        all_books = book.objects.all()
        return render(request,'index.html', {'all':all_books})
    all_books = book.objects.all()
    return render(request,'index.html', {'all':all_books})

def books(request,number):
    if request.method == "POST":
        new_author = author.objects.get(id=request.POST['auth_select'])
        selec_book = book.objects.get(id=number)
        selec_book.authors.add(new_author)
        selec_authors = author.objects.filter(books=selec_book)
        not_authors = author.objects.exclude(books=selec_book)
        all_authors = author.objects.all()
        context = {
            'selecbook':selec_book,
            'selecauthor':selec_authors,
            'allauthors': all_authors,
            'notauthors': not_authors
            }
        return render(request,'books.html', context)
    selec_book = book.objects.get(id=number)
    selec_authors = author.objects.filter(books=selec_book)
    not_authors = author.objects.exclude(books=selec_book)
    all_authors = author.objects.all()
    context = {
            'selecbook':selec_book,
            'selecauthor':selec_authors,
            'allauthors': all_authors,
            'notauthors': not_authors
            }
    return render(request,'books.html', context)

def IndexAuthors(request):
    if request.method == "POST":
        author.objects.create(first_name=request.POST['firstname'],last_name=request.POST['lastname'],notas=request.POST['notas'])
        all_authors = author.objects.all()
        return render(request,'authors_index.html', {'all':all_authors})
    all_authors = author.objects.all()
    return render(request,'index_authors.html', {'all':all_authors})

def authors(request,number):
    if request.method == "POST":
        new_book = book.objects.get(id=request.POST['auth_select'])
        selec_author = author.objects.get(id=number)
        selec_author.books.add(new_book)
        selec_books = book.objects.filter(authors=selec_author)
        not_books = book.objects.exclude(authors=selec_author)
        all_books = book.objects.all()
        context = {
            'selecauthor':selec_author,
            'selecbook':selec_books,
            'allbooks': all_books,
            'notbooks': not_books
            }
        return render(request,'authors.html', context)
    selec_author = author.objects.get(id=number)
    selec_books = book.objects.filter(authors=selec_author)
    not_books = book.objects.exclude(authors=selec_author)
    all_books = book.objects.all()
    context = {
            'selecauthor':selec_author,
            'selecbook':selec_books,
            'allbooks': all_books,
            'notbooks': not_books
            }
    return render(request,'authors.html', context)