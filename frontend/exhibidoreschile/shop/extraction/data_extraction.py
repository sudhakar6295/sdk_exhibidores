from shop.models import Products
import json

def fetch_categories():
    unique_categories = Products.objects.values_list('category', flat=True).distinct()
    return unique_categories