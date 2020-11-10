# Generated by Django 3.1 on 2020-08-21 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dispatch_time', models.DateTimeField()),
                ('cooler_box', models.CharField(max_length=40)),
            ],
        ),
        migrations.CreateModel(
            name='DispenserCoolerBox',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('box_number', models.IntegerField()),
                ('location', models.CharField(max_length=50)),
                ('unlock_code', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='ShippingProvider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('date_joined', models.DateField()),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.IntegerField()),
                ('transport_mode', models.CharField(max_length=60)),
            ],
        ),
    ]