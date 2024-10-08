from django.db import models
from django.utils import timezone

class Products(models.Model):
    
    sku = models.CharField(max_length=255)
    url_scraped = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    percent_discount = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    price_discount = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    tax = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    price_included_taxes = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    price_mt2 = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    price_mtl = models.DecimalField(max_digits=10, decimal_places=4, null=True, blank=True)
    stock_1 = models.IntegerField(null=True, blank=True)
    stock_2 = models.IntegerField(null=True, blank=True)
    stock_3 = models.IntegerField(null=True, blank=True)
    stock_comentarie_1 = models.CharField(max_length=100, null=True, blank=True)
    stock_comentarie_2 = models.CharField(max_length=100, null=True, blank=True)
    stock_comentarie_3 = models.CharField(max_length=100, null=True, blank=True)
    images = models.JSONField(null=True, blank=True)  # Requires Django 3.1+
    route_product1 = models.CharField(max_length=255,null=True, blank=True)
    route_product2 = models.CharField(max_length=255,null=True, blank=True)
    route_product3 = models.CharField(max_length=255,null=True, blank=True)
    route_product4 = models.CharField(max_length=255,null=True, blank=True)
    route_product5 = models.CharField(max_length=255,null=True, blank=True)
    route_product6 = models.CharField(max_length=255,null=True, blank=True)
    route_product7 = models.CharField(max_length=255,null=True, blank=True)
    route_product8 = models.CharField(max_length=255,null=True, blank=True)
    route_product9 = models.CharField(max_length=255,null=True, blank=True)
    route_product10 = models.CharField(max_length=255,null=True, blank=True)
    short_description = models.TextField(null=True, blank=True)
    long_description = models.TextField(null=True, blank=True)
    pdf = models.TextField(null=True, blank=True)
    length = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    width = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    weight = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    main_color = models.CharField(max_length=255, null=True, blank=True)
    glossy_or_matte = models.CharField(max_length=50, null=True, blank=True)
    main_material = models.CharField(max_length=255, null=True, blank=True)
    origen = models.CharField(max_length=255, null=True, blank=True)
    last_scraped_date = models.DateTimeField(auto_now=True)
    updated_date = models.DateTimeField(auto_now=True)
    created_date = models.DateTimeField(default=timezone.now)
    status = models.CharField(max_length=50, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)
    specifications = models.JSONField(null=True, blank=True)  # Requires Django 3.1+

    def __str__(self):
        return self.sku
    
    class Meta:
        db_table = 'products'
