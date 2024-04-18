from django.shortcuts import render, redirect
from django.utils import timezone
from datetime import timedelta
from .models import Client, Product, Buy 
from .forms import ProductForm

def index(request):
    return render(request, 'shop6_app/index.html')

def client_buy(request, client_id):
    client = Client.objects.get(pk=client_id)

    buy_last_7_days = client.buy_set.filter(buy_data_gte=timezone.now() - timedelta(days=7))
    buy_last_30_days = client.buy_set.filter(buy_data_gte=timezone.now() - timedelta(days=30))
    buy_last_365_days = client.buy_set.filter(buy_data_gte=timezone.now() - timedelta(days=365))

    all_products = Product.objects.all()

    if request.method == 'POST':
        product_form = ProductForm(request.POST, request.FILES)
        if product_form.is_valid():
            new_product = product_form.save()

            return redirect('client_buy', client_id=Client.id)
        
    else:
        product_form = ProductForm()

    context = {
        'client': client,
        'buy_last_7_days': buy_last_7_days,
        'buy_last_30_days': buy_last_30_days,
        'buy_last_365_days': buy_last_365_days,
        'all_products': all_products,
        'product_form': product_form,
    }

    return render(request, 'shop6_app/client_buy.html', context)