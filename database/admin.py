from django.contrib import admin
from .models import *
from django.forms import ModelForm
from django.http import HttpResponse, HttpResponseRedirect
# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
