from django.shortcuts import render, redirect
from .models import Item, List
from django.views.decorators.csrf import csrf_exempt


def home_page(request):
    '''домашняя страница'''
    return render(request, 'home.html')

def view_list(request, list_id):
    '''представление списка'''
    list_ = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': list_})

@csrf_exempt
def new_list(request):
    '''новый список'''
    list_ = List.objects.create()
    list_.save()
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

@csrf_exempt
def add_item(request, list_id):
    '''добавить элемент'''
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')