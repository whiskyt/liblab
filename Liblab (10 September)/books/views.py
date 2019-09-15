from django.shortcuts import render,get_object_or_404
from .models import Books
from django.db.models import Q
# Create your views here.

def display_view(request):
    data = Books.objects.all()

    query = request.GET.get('q')
    if query:
        data = data.filter(
            Q(name__icontains=query) |
            Q(author__icontains=query) |
            Q(genre__icontains=query) |
            Q(category__icontains=query)

            ).distinct()

    context = {'data':data}
    return render(request,'templates/books/display.html',context)

def detail(request,book_id):
    instance = get_object_or_404(Books,id=book_id)
    return render(request,'templates/books/detail.html',{'instance':instance})