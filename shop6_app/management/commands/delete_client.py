from django.core.management.base import BaseCommand
from shop6_app.models import Client 

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('pk', type=int)

    def mange(self, *args, **kwargs):

        pk = kwargs.get('pk')
        client = Client.objects.filter(pk=pk).first()
        if client is not None:
            client.delete()

        self.stdout.write(self.style.WARNING(f'Клиент успешно удален: {client}')) 