import os
from django.shortcuts import render
from .models import Products

# Create your views here.
def home(request):
    
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from .models import Products
import os

def Add_product(request):
    if request.method == 'POST':
        name = request.POST.get('Product_Name')
        image = request.FILES.get('Product_image')
        description = request.POST.get('Product_Description')
        price = request.POST.get('Product_price')
        stock = request.POST.get('Product_stock')

        product = Products(
            name=name,
            image=image,
            description=description,
            price=price,
            stock=stock
        )
        product.save()

        # data size
        total_bytes = 0
        total_bytes += len(name.encode('utf-8'))
        total_bytes += len(description.encode('utf-8'))
        total_bytes += len(str(price).encode('utf-8'))
        total_bytes += len(str(stock).encode('utf-8'))

        if product.image and product.image.path and os.path.exists(product.image.path):
            total_bytes += os.path.getsize(product.image.path)

        total_mb = round(total_bytes / (1024 * 1024), 2)
        product.data_size = total_mb
        product.save()

        return redirect('list_products')
    return render(request, 'add_product.html')


# def list_products(request):
#     products = Products.objects.all()
#     product_data = []
#     for product in products:
#         total_bytes = 0
#         total_bytes += len(product.name.encode('utf-8'))
#         total_bytes += len(product.description.encode('utf-8'))
#         total_bytes += len(str(product.price).encode('utf-8'))
#         total_bytes += len(str(product.stock).encode('utf-8')) 

#         if product.image and product.image.path and os.path.exists(product.image.path):
#             total_bytes += os.path.getsize(product.image.path)
#         total_mb = round(total_bytes / (1024 * 1024), 2)

#         product_data.append({
#             'id': product.id,
#             'name': product.name,
#             'image': product.image,
#             'description': product.description,
#             'price': product.price,
#             'stock': product.stock,
#             'data_size_mb': total_mb
#         })
#     return render(request, 'list_products.html', {'products': product_data})
def list_products(request):
    products = Products.objects.all()
    return render(request, 'list_products.html', {'products': products})
