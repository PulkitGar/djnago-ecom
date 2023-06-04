from django.shortcuts import render
from .models import Product
from django.shortcuts import get_object_or_404
from category.models import Category





# Create your views here.

def store(request, category_slug=None):

    categories = None
    products = None

    if category_slug != None:
        categories =get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(category=categories, is_available=True)
        product_count = products.count()

    else:
        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
        
    context = {'products': products,
               'product_count': product_count,
               }
    return render(request, 'store/store.html', context)
   

def product_detail(request, category_slug, product_slug):

    product_category = Category.objects.get(slug=category_slug)
    print(product_category.category_name)
   
    single_product = Product.objects.get(category=product_category.id, slug=product_slug)
    print(single_product)

    context={
        'single_product': single_product
    }

    return render(request, 'store/product_details.html', context)   