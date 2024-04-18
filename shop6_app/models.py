from django.db import models
from django.utils import timezone

class Client(models.Model):
    name = models.CharField(max_length=300)
    email = models.EmailField()
    phone_num = models.CharField(max_length=20)
    addres = models.TextField()
    registration_data = models.DateField(default=timezone.now)

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=10)
    quantity = models.PositiveIntegerField()
    added_data = models.DateField(default=timezone.now)
    photo = models.ImageField(upload_to='product_photos', null=True, blank=True)

    def __str__(self):
        return self.name
    
class Buy(models.Model):
    client = models.ForeignKey(Client, on_delete= models.CASCADE)
    products = models.ManyToManyField(Product)
    total_amount = models.DecimalField(decimal_places=2, max_digits=10)
    buy_data = models.DateField(default=timezone.now)

    def _str_(self):
        return f'Buy {self.id} by {self.client.name}'