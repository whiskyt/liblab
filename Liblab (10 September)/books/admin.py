from django.contrib import admin
from .models import Books
from django.shortcuts import render
from datetime import datetime, timezone
from django.db.models import Q
# Register your models here.


def book_out(modeladmin,request,queryset):
    for b in queryset:
        b.in_lib = False
        b.save()
book_out.short_description = 'Process book/books being taken out'

def book_in(modeladmin,request,queryset):
    for b in queryset:
        b.in_lib = True
        b.save()
book_in.short_description = 'Process book/books being returned'

def display_books_out(modeladmin,request,queryset):
    items = Books.objects.all()
    form = []
    for b in items:
        if not b.in_lib:
            form.append(b)
    return render(request,'templates/books/books_out.html',{'form':form})
display_books_out.short_description = 'report of books out on loan'

def books_overdue(modeladmin,request,queryset):
    items = Books.objects.all()
    form = []
    two_weeks = 14*24*3600
    for b in items:
        delt = datetime.now(timezone.utc) - b.time
        if delt.total_seconds() > two_weeks:
            form.append(b)
    return render(request,'templates/books/books_overdue.html',{'form':form})
books_overdue.short_description= 'report of books overdue'

'''
def cur_category():
    arr = Books.objects.all()
    categories = []
    for i in arr:
        categories.append(i.category)
    categories = list(dict.fromkeys(categories))
    return categories'''

def remove_cat(modeladmin,request,queryset):
    for b in queryset:
        b.category='None'
        b.save()
remove_cat.short_description= 'remove category of book/books'

def add_cat(modeladmin,request,queryset):

    query = request.GET.get('q')
    for b in queryset:
        b.category=query
        b.save()

    return render(request,'templates/books/form.html',{})
add_cat.short_description='add category to book/books'


    
class BooksAdmin(admin.ModelAdmin):
    list_display = ['name','author','genre','summary','category','time','in_lib']
    actions = [book_out,book_in,display_books_out,books_overdue,remove_cat,add_cat,]

admin.site.register(Books,BooksAdmin)