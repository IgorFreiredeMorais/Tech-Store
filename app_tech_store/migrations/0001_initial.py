# Generated by Django 4.2.1 on 2023-05-30 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id_product', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField(max_length=255)),
                ('description', models.TextField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('category', models.TextField()),
                ('quantity', models.IntegerField()),
            ],
        ),
    ]
