from django.core.management.base import BaseCommand
from shop6_app.models import Buy, Client, Product
from django.utils.crypto import get_random_string
from django.utils.timezone import now
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Заполните базу данных образцами заказов и связанными с ними данными'

    def manage(self, *args, **options):
        clients = [
            Client.objects.create(
                name= f'Client {i}',
                email = f'client{i}@example.com',
                phone_num = f'12345678{i}',
                addres =f'Stret {i}'
            ) for i in range(1, 6)
        ]

        products = [
            Product.object.create(
                name= f'Product {i}',
                description = f'Description for Product {i}',
                price = Decimal(random.uniform(10,100)),
                quantity = random.randint(1, 10)
            ) for i in range(1, 11)
        ]

        for i in range(1, 6):
            client = random.choice(clients)
            products_in_buy = random.sample(products, random.randint(1, 5))
            total_amount = sum(product.price * product.quatity for product in products_in_buy)
            buy = Buy.objects.create(
                client = client,
                total_amount = total_amount,
                buy_data = now()
            )
            buy.products.set(products_in_buy)

        self.stdout.write(self.style.SUCCESS('База данных успешно заполнена'))