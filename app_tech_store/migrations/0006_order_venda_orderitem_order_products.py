# Generated by Django 4.2.1 on 2023-06-05 01:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_tech_store', '0005_category_manufacturer_product_manufacturer_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tech_store.client')),
            ],
        ),
        migrations.CreateModel(
            name='Venda',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tech_store.client')),
                ('products', models.ManyToManyField(to='app_tech_store.product')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tech_store.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_tech_store.product')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(through='app_tech_store.OrderItem', to='app_tech_store.product'),
        ),
    ]