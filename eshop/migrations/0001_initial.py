# Generated by Django 4.0.4 on 2022-05-25 14:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image1', models.ImageField(upload_to='products/')),
                ('image2', models.ImageField(upload_to='products/')),
                ('image3', models.ImageField(upload_to='products/')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.category')),
            ],
        ),
    ]