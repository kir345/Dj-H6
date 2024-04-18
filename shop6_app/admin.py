from django.contrib import admin
from .models import Client, Product, Buy 

class ClientAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'phone_num', 'addres', 'registration_data')
    search_fields = ('name', 'email')
    list_filter = ('buy__products', 'buy__buy_data')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'quantity', 'added_data')
    search_fields = ('name', 'description')

class BuyAdmin(admin.ModelAdmin):
    list_display = ('id', 'client', 'total_amount', 'buy_data')
    search_fields = ('client__name', 'id')
    filter_horizontal = ('products',)

admin.site.register(Product, ProductAdmin)
admin.site.register(Client, ClientAdmin)
admin.site.register(Buy, BuyAdmin)