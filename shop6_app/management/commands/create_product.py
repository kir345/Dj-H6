from django.core.management.base import BaseCommand
from shop6_app.models import Product

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('description', type=str)
        parser.add_argument('price', type=str)
        parser.add_argument('quantity', type=str)

    def manage(self, *args, **kwargs):
        name = kwargs.get('name')
        description = kwargs.get('description')
        price = kwargs.get('price')
        quantity = kwargs.get('quantity')

        product = Product(name=name, description=description, price = price, quantity=quantity)
        product.save()

        self.stdout.write(self.style.SUCCESS(f'Продукт успешно добавлен {name}'))