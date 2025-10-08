from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render, redirect, get_object_or_404
from main.forms import ProductForm
from main.models import Product
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse
from django.urls import reverse
import json


@login_required(login_url='/login')
def show_main(request):
    filter_type = request.GET.get("filter", "all")  # default 'all'

    if filter_type == "all":
        products_list = Product.objects.all()
    else:
        products_list = Product.objects.filter(user=request.user)

    context = {
        'npm' : '2406423276',
        'name': request.user.username,
        'class': 'PBP B',
        'products_list': products_list,
        'last_login': request.COOKIES.get('last_login', 'Never')
    }

    return render(request, "main.html", context)

def create_product(request):
    form = ProductForm(request.POST or None)

    if form.is_valid() and request.method == "POST":
        product_entry = form.save(commit = False)
        product_entry.user = request.user
        product_entry.save()
        return redirect('main:show_main')

    context = {'form': form}
    return render(request, "create_product.html", context)

@login_required(login_url='/login')
def show_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.increment_views()

    context = {
        'product': product,
        'product_id': str(id)
    }
    return render(request, "product_detail.html", context)


def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))

def show_xml(request):
     products_list = Product.objects.all()
     xml_data = serializers.serialize("xml", products_list)
     return HttpResponse(xml_data, content_type="application/xml")

def show_json(request):
    products_list = Product.objects.all()
    data = [
        {
            'id': str(product.id),
            'name': product.name,
            'price': product.formatted_price(),
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'is_featured': product.is_featured,
            'user_id': product.user_id,
        }
        for product in products_list
    ]

    return JsonResponse(data, safe=False)

def show_xml_by_id(request, product_id):
   try:
       product_item = Product.objects.filter(pk=product_id)
       xml_data = serializers.serialize("xml", product_item)
       return HttpResponse(xml_data, content_type="application/xml")
   except Product.DoesNotExist:
       return HttpResponse(status=404)

def show_json_by_id(request, product_id):
    try:
        product = Product.objects.select_related('user').get(pk=product_id)
        data = {
            'id': str(product.id),
            'name': product.name,
            'description': product.description,
            'category': product.category,
            'thumbnail': product.thumbnail,
            'product_views': product.product_views,
            'price': product.formatted_price(),
            'is_featured': product.is_featured,
            'user_id': product.user_id,
            'user_username': product.user.username if product.user_id else None,
        }
        return JsonResponse(data)
    except Product.DoesNotExist:
        return JsonResponse({'detail': 'Not found'}, status=404)


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been successfully created!')
            return redirect('main:login')
    context = {'form':form}
    return render(request, 'register.html', context)

def ajax_register(request):
    if request.method == 'POST':
        try:
            # Parse data JSON dari body request
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password1')
            password_confirm = data.get('password2')
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)

        # Gunakan UserCreationForm untuk validasi yang konsisten
        form = UserCreationForm(data={'username': username, 'password': password, 'password2': password_confirm})
        
        if form.is_valid():
            try:
                # Simpan pengguna baru
                form.save()
                return JsonResponse({
                    'status': 'success', 
                    'message': 'Account created successfully! Please log in.', 
                    # Anggap URL login Anda adalah 'main:login'
                    'redirect_url': reverse('main:login') 
                }, status=201)
            except Exception:
                 # Tangani kegagalan penyimpanan yang tidak terduga
                 return JsonResponse({'status': 'error', 'message': 'Could not save user.'}, status=500)
        else:
            # Ekstrak pesan error pertama untuk ditampilkan
            errors = dict(form.errors)
            first_error_message = next(iter(errors.values()))[0]
            return JsonResponse({'status': 'error', 'message': f'{first_error_message}'}, status=400)

    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)


def login_user(request):
   if request.method == 'POST':
      form = AuthenticationForm(data=request.POST)

      if form.is_valid():
        user = form.get_user()
        login(request, user)
        response = HttpResponseRedirect(reverse("main:show_main"))
        response.set_cookie('last_login', str(datetime.datetime.now()))
        return response

   else:
      form = AuthenticationForm(request)
   context = {'form': form}
   return render(request, 'login.html', context)

def ajax_login(request):
    if request.method == 'POST':
        try:
            # Parse data JSON dari body request
            data = json.loads(request.body)
            username = data.get('username')
            password = data.get('password')
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON format'}, status=400)

        # Otentikasi Pengguna
        user = authenticate(request, username=username, password=password)

        if user is not None:
            # Login berhasil dan buat sesi
            login(request, user)
            
            # Kembalikan URL pengalihan
            return JsonResponse({
                'status': 'success', 
                'message': f'Welcome back, {username}!', 
                # Anggap URL utama Anda adalah 'main:show_main'
                'redirect_url': reverse("main:show_main") 
            }, status=200)
        else:
            # Login gagal
            return JsonResponse({
                'status': 'error', 
                'message': 'Invalid username or password.'
            }, status=401)
            
    return JsonResponse({'status': 'error', 'message': 'Method not allowed'}, status=405)

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('main:login'))
    response.delete_cookie('last_login')
    return response

def edit_product(request, id):
    product = get_object_or_404(Product, pk=id)
    form = ProductForm(request.POST or None, instance=product)
    if form.is_valid() and request.method == 'POST':
        form.save()
        return redirect('main:show_main')

    context = {
        'form': form
    }

    return render(request, "edit_product.html", context)

def delete_product(request, id):
    product = get_object_or_404(Product, pk=id)
    product.delete()
    return HttpResponseRedirect(reverse('main:show_main'))