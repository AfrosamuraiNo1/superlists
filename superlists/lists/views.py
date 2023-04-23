from django.shortcuts import render, redirect
from .models import Item, List
from django.views.decorators.csrf import csrf_exempt
from django.core.exceptions import ValidationError
from lists.forms import ItemForm


def home_page(request):
    '''домашняя страница'''
    return render(request, 'home.html', {'form': ItemForm()})

@csrf_exempt
def view_list(request, list_id):
    '''представление списка'''
    list_ = List.objects.get(id=list_id)
    form = ItemForm()
    if request.method == 'POST':
        form = ItemForm(data=request.POST)
    if form.is_valid():
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    return render(request, 'list.html', {'list': list_, "form": form})

@csrf_exempt
def new_list(request):
    '''новый список'''
    form = ItemForm(data=request.POST)
    if form.is_valid():
        list_ = List.objects.create()
        Item.objects.create(text=request.POST['text'], list=list_)
        return redirect(list_)
    else:
        return render(request, 'home.html', {"form": form})

