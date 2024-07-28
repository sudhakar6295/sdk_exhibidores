from shop.models import Products
from django.db.models import Q
import json
import os,requests

def fetch_categories():
    unique_categories = Products.objects.values_list('route_product1', flat=True).distinct()
    return unique_categories



def products_in_category(category):

    products = Products.objects.filter(
        Q(route_product1=category) | 
        Q(route_product2=category) | 
        Q(route_product3=category) | 
        Q(route_product4=category) | 
        Q(route_product5=category) | 
        Q(route_product6=category)
    ).values('name', 'price', 'sku','images')

    product_data = []
    for product in products:
        try:
            product_images = product.get('images')
            key  = list(product_images.keys())
            save_image(list(product_images.values()))
            save_image([product_images.get(key[0])])
            product_image = product_images.get(key[0]).split('/')[-1]
        except :
             product_image = None 
        product_info = {
            'name': product.get('name'),
            'price': product.get('price'),
            'sku': product.get('sku'),
            'image_url': product_image  # Example URL based on SKU
        }
        product_data.append(product_info)

    return product_data

def check_file_in_folder(folder, file):
        # Check if the file exists in the given folder
        if os.path.exists(os.path.join(folder,file)):
            return True
        else:
            return False

def save_image( temp_images,folder="static/images"):
        for url in temp_images:
            file_name = url.split('/')[-1]
            abs_url = url
            if not os.path.exists(folder):
                        os.makedirs(folder)
            file_exits = check_file_in_folder(folder, file_name)
            if  file_exits:
                continue
            file_name = url.split('/')[-1]
            filepath = os.path.join(folder,file_name)
            
            response = requests.get(abs_url)
            if response.status_code == 200:
                with open(filepath, 'wb') as f:
                    f.write(response.content)
                    print(f"Image saved as {filepath}")
            else:
                print(f"Failed to download image from {filepath}")  

def get_image_name(images):

    abs_image = []
    for i in  images:
          abs_image.append(i.split('/')[-1])
    return abs_image

def generate_html(data):
    html_content = ''
    for key, value in data.items():
        html_content += f'<p><strong>{key}</strong>: {value}</p>\n'

    return html_content

def get_product_data(sku):

    product_data = Products.objects.filter(sku=sku).first()
    images = list(product_data.images.values())
    save_image(images)
    abs_image = get_image_name(images)
    specifications_html = generate_html(product_data.specifications)

    return product_data,abs_image,specifications_html

def search_product(query):
     
    product_data = Products.objects.filter(
        Q(name=query) | Q(sku=query)
    ).first()
 
    if product_data:
        
        images = list(product_data.images.values())
        save_image(images)
        abs_image = get_image_name(images)
        specifications_html = generate_html(product_data.specifications)

        return product_data,abs_image,specifications_html
    
        