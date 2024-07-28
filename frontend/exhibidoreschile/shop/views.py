from django.shortcuts import render
from shop.extraction.data_extraction import fetch_categories
# Create your views here.

def index(request):
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})


def search(request):
    return render(request, 'index.html')

