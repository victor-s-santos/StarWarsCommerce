from django.shortcuts import render, redirect
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView, ListView
from django.utils.decorators import method_decorator

@method_decorator(login_required(), name='dispatch')
class ProductList(ListView):
    model = Product


@login_required
def product_list(request):
    """Product List"""
    products = Product.objects.all()
    return render(request, 'commerce/product_list.html', {"products": products})

@login_required
def order_list(request):
    """Order List"""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'commerce/order_list.html', {"orders": orders})

"""class OrderDeleteView(DeleteView):
    model = Order
"""

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
            return render(request, 'commerce/product_order.html', {'form': form})
    else:
        form = OrderForm()
    return render(request, 'commerce/product_order.html', {'form': form})
