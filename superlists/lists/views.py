from django.shortcuts import render
from django.http import HttpResponse

# Создайте здесь представления свои.
def home_page(request):
    return HttpResponse('<html><title>To-Do lists</title></html>')