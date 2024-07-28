from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name= 'index'),
    path('search/', views.search, name='search'),
    path('category/<str:category>',views.category, name='category'),
    path('product/<str:sku>',view=views.product,name='product')
]