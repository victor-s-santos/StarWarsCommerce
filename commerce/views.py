from django.shortcuts import render, redirect
from .models import Product
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required

@login_required
def product_list(request):
    """Product List"""
    products = Product.objects.all()
    return render(request, 'commerce/product_list.html', {"products": products})

@staff_member_required
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

@login_required
def product_order(request):
    """Product Orders"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            return redirect('product_order')
        else:
            messages.error(request, 'Bad profitability or invalid amount.')
            return render(request, 'commerce/product_order.html', {'form': form})
    else:
        form = OrderForm()
    return render(request, 'commerce/product_order.html', {'form': form})
