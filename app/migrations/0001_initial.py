# Generated by Django 4.0.5 on 2022-06-09 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('product_pic', models.ImageField(upload_to='product_img')),
                ('description', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Virtual Company Ltd.', max_length=50)),
                ('address', models.CharField(default='23th Street, Zbcxyz', max_length=150)),
                ('phone', models.IntegerField(default='+91 900XX XX XXX')),
                ('email', models.CharField(default='abc@xompany.com', max_length=150)),
            ],
        ),
    ]