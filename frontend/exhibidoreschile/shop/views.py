from django.shortcuts import render
from shop.extraction.data_extraction import fetch_categories,products_in_category,get_product_data,search_product
# Create your views here.
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})


def search(request):
    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET['query']
        product_data,images,specifications_html =  search_product(query)
        if product_data:
            return render(request, 'product_detail.html',{'product':product_data,'images':images,'specifications_html':specifications_html})

    categorys = fetch_categories()
    return render(request, 'index.html',{'categorys':categorys})

def category(request,category):
    products = products_in_category(category)
    total_products = len(products)
    page = request.GET.get('page', 1)
    page_count = 16
    paginator = Paginator(products, 15)
    try:
        items = paginator.page(page)
        page_count = len(items)
    except PageNotAnInteger:
        items = paginator.page(1)
        page_count = len(items)
    except EmptyPage:
        items = paginator.page(paginator.num_pages)

    return render(request, 'products.html',{'products':items,'page':items,'page_count':page_count,'total_products':total_products})


def product(request,sku):

    product_data,images,specifications_html = get_product_data(sku)
    return render(request, 'product_detail.html',{'product':product_data,'images':images,'specifications_html':specifications_html})

