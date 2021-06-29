from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from .forms import CustomUserForm
from .models import Category, Product


# Create your views here.


def product_list(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True)
    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    return render(request, 'shop/product/list.html',
                  {'category': category, 'categories': categories,
                   'products': products})

def product_detail(request, id, slug):
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    return render(request, 'shop/product/detail.html', {'product': product})

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('shop:index')
        else:
            messages.info(request, 'Try again! username or password is incorrect')
    context = {}
    return render(request, 'shop/login.html', context)
def logout_page(request):
    logout(request)
    return redirect('shop:index')

@login_required(login_url='shop:login')

def register_page(request):
    if request.method != 'POST':
        form = CustomUserForm()
    else:
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('shop:login')
    context = {'form': form}
    return render(request, 'shop/register.html', context)

def index(request):
    return render(request, 'shop/index.html')


