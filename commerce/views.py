from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from .models import Product, Order
from .forms import ProductForm, OrderForm
from django.contrib import messages
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.auth.decorators import login_required
from cloudinary.forms import cl_init_js_callbacks      

@login_required
def product_list(request):
    """Product List"""
    products = Product.objects.all()
    return render(request, 'commerce/product_list.html', {"products": products})

@login_required
def detail_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'commerce/product_detail.html', {'product': product})

@staff_member_required
def product_edit(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES, instance=product)
        if form.is_valid():
            product = form.save(commit=False)
            product.published_date = timezone.now()
            product.save()
            return redirect('commerce:detail_product', pk=product.pk)
        else:
            messages.error(request, 'Invalid Values.')
            return render(request, 'commerce/product_edit.html', {'form': form})
    else:
        form = ProductForm(instance=product)
    return render(request, 'commerce/product_edit.html', {'form': form})


@staff_member_required
def product_register(request):
    """Register Products"""
    if request.method == 'POST':
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            product = form.save(commit=False)
            product.user = request.user
            product.save()
            messages.success(request, 'You have successfully registered a product!')
            return redirect('commerce:product_register')
        else:
            return render(request, 'commerce/product_register.html', {'form': form})
    else:
        form = ProductForm()
    return render(request, 'commerce/product_register.html', {'form': form})

@staff_member_required
def product_remove(request, pk):
    """Remove product"""
    product = get_object_or_404(Product, pk=pk)
    name = product.product_name
    product.delete()
    messages.success(request, f'The product:{name} has been deleted successfully.')
    return redirect('commerce:product_list')

@login_required
def order_list(request):
    """Order List"""
    orders = Order.objects.filter(user=request.user)
    return render(request, 'commerce/order_list.html', {"orders": orders})

@login_required
def register_order(request):
    """Product Orders"""
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            messages.success(request, 'You have successfully registered order from the product!')
            return redirect('commerce:register_order')
        else:
            return render(request, 'commerce/register_order.html', {'form': form})
    else:
        form = OrderForm()
    return render(request, 'commerce/register_order.html', {'form': form})

@login_required
def order_detail(request, pk):
    """Order detail"""
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'commerce/order_detail.html', {'order': order})

@login_required
def order_edit(request, pk):
    """Edit Order"""
    order = get_object_or_404(Order, pk=pk)
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.published_date = timezone.now()
            order.save()
            messages.success(request, 'You have successfully updated order from the product!')
            return redirect('commerce:order_detail', pk=order.pk)
        else:
            return render(request, 'commerce/order_edit.html', {'form': form})
    else:
        form = OrderForm(instance=order)
    return render(request, 'commerce/order_edit.html', {'form': form})

@login_required
def order_remove(request, pk):
    """Remove Order"""
    order = get_object_or_404(Order, pk=pk)
    name = order.product_name
    order.delete()
    messages.success(request, f'The order of the product:{name} has been deleted successfully.')
    return redirect('commerce:order_list')