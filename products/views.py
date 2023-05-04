from django.http import HttpResponse
from django.shortcuts import render
from.models import Product


# Create your views here.

def index(request):
    products = Product.objects.all()
    return render(request, 'index.html', {'products': products}) 

def new(request):
    return HttpResponse('New Products')

# def new_arrivals(requet):
#     return HttpResponse('zimefika')

# add to cart view
# from django.shortcuts import redirect, get_object_or_404
# from django.contrib import messages

# from .models import Product, CartItem
# from .cart import Cart

# def add_to_cart(request, product_id):
#     product = get_object_or_404(Product, id=product_id)
#     cart = Cart(request)
#     quantity = request.POST.get('quantity', 1)
#     cart.add(product=product, quantity=quantity)
#     messages.success(request, f"{product.name} has been added to your cart.")
#     return redirect('cart')
