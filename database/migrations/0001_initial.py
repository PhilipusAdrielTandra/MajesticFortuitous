# Generated by Django 4.1.3 on 2022-12-09 13:29

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('FirstName', models.CharField(max_length=100)),
                ('LastName', models.CharField(max_length=100)),
                ('PhoneNumber', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='nonPerishables',
            fields=[
                ('id', models.IntegerField(max_length=12, primary_key=True, serialize=False)),
                ('ItemName', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='files/images')),
                ('Price', models.IntegerField(max_length=6)),
                ('Stock', models.IntegerField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Perishables',
            fields=[
                ('id', models.IntegerField(max_length=12, primary_key=True, serialize=False)),
                ('ItemName', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='files/images')),
                ('Price', models.IntegerField(max_length=6)),
                ('Stock', models.IntegerField(max_length=3)),
                ('Expiry', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(blank=True, default=datetime.datetime)),
                ('noperish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.nonperishables')),
                ('perish', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='database.perishables')),
            ],
        ),
    ]
