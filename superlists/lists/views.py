from django.shortcuts import render, redirect
from .models import Item

def home_page(request):
    '''домашняя страница'''
    return render(request, 'home.html')

def view_list(request):
    '''представление списка'''
    items = Item.objects.all()
    return render(request, 'list.html', {'items': items})

def new_list(request):
    '''новый список'''
    item = Item.objects.create(text=request.POST['item_text'])
    item.save()
    return redirect('/lists/the-only-list-in-the-world/')