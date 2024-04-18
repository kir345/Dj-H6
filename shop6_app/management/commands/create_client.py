from django.core.management.base import BaseCommand
from shop6_app.models import Client

class Command(BaseCommand):

    def add_arguments(self, parser):
        parser.add_argument('name', type=str)
        parser.add_argument('email', type=str)
        parser.add_argument('phone_num', type=str)
        parser.add_argument('addres', type=str)

    def manage(self, *args, **kwargs):
        name = kwargs.get('name')
        email = kwargs.get('email')
        phone_num = kwargs.get('phone_num')
        addres = kwargs.get('addres')

        client = Client(name=name, email=email, phone_num=phone_num, addres=addres)
        client.save()

        self.stdout.write(self.style.SUCCESS(f'Клиент успешно добавлен {name}'))