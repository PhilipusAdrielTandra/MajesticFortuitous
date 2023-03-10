# Generated by Django 4.1.3 on 2023-01-01 02:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('database', '0002_alter_membership_phonenumber_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Complete', models.BooleanField(default=False, null=True)),
                ('Transaction_id', models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Quantity', models.IntegerField(blank=True, default=0, null=True)),
                ('Date', models.DateTimeField(auto_now_add=True)),
                ('Order', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.order')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemName', models.CharField(max_length=100)),
                ('Image', models.ImageField(upload_to='')),
                ('Price', models.FloatField()),
                ('Stock', models.IntegerField()),
                ('Expiry', models.DateField(null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='noperish',
        ),
        migrations.RemoveField(
            model_name='transactions',
            name='perish',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='FirstName',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='LastName',
        ),
        migrations.RemoveField(
            model_name='membership',
            name='PhoneNumber',
        ),
        migrations.AddField(
            model_name='membership',
            name='Email',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='Name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='membership',
            name='User',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='nonPerishables',
        ),
        migrations.DeleteModel(
            name='Perishables',
        ),
        migrations.DeleteModel(
            name='Transactions',
        ),
        migrations.AddField(
            model_name='orderitem',
            name='Product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='Member',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='database.membership'),
        ),
    ]
