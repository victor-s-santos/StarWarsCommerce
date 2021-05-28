from django.shortcuts import render
from .models import Product
from .forms import ProductForm
from django.contrib import messages

def product_list(request):
    """Product List"""
    products = Product.objects.all()
    return render(request, 'commerce/product_list.html', {"products": products})

def product_register(request):
    """Register Products"""
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'You have successfully registered a product!')
            return redirect('product_register')
        else:
            messages.error(request, 'Email or username already registered.')
            return render(request, 'commerce/product_register.html', {'form': form})
    else:
        form = ProductForm()
    return render(request, 'commerce/product_register.html', {'form': form})
