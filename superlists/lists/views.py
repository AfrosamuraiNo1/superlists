from django.shortcuts import render, redirect
from .models import Item

def home_page(request):
    '''домашняя страница'''
    if request.method == 'POST':
        item = Item.objects.create(text=request.POST['item_text'])
        item.save()
        return redirect('/')
    items = Item.objects.all()
    return render(request, 'home.html', {'items': items})