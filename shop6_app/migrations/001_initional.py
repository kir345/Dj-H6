import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models

class Migration(migrations.Migration):

    initional = True

    dependencies = []
    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('email', models.EmailField(max_length=300)),
                ('phone_num', models.CharField(max_length=20)),
                ('addres', models.TextField()),
                ('registration_data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('description', models.TextField()),
                ('price', models.DecimalField( max_digits=10, decimal_places=2)),
                ('quantity', models.PositiveIntegerField()),
                ('added_data', models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Buy',
            fields=[
               ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_amount', models.DecimalField(max_digits=10, decimal_places=2)),
                ('buy_data', models.DateField(auto_now_add=True)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop_app.client')),
                ('products', models.ManyToManyField(to='shop_app.product')),
            ],
        ),
    ]