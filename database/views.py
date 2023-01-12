from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib import messages
from django.contrib.auth import logout, login
from .models import *
import json
# Create your views here.
#Creates the /cart page and essentially renders cart.html and also uses the order model from the models.py folder
def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, "database/cart.html", context)
#Similar to the cart page as it also just shows all of the carts contents and prices but uses a different html being checkout.html
def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    context = {'items': items, 'order': order, 'cartItems':cartItems}
    return render(request, "database/checkout.html", context)
#Creates the store page, this takes from the products database from the models.py file and loads up store.html
def store(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        messages.success(request, ("You are not logged in and as a result, cannot buy any items"))
        items = []
        order = {'get_cart_total': 0, 'get_cart_items': 0}
        cartItems = order['get_cart_items']
    products = Product.objects.all()
    context = {'products': products, 'cartItems': cartItems}
    return render(request, "database/store.html", context)
#Requests from cart.js and essentially uses it as instructions in order to create requests from the database well as creates that 'add' action for the different features in the app
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)
    customer = request.user.customer
    product = Product.objects.get(id = productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)
    #Add function based on action
    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)
    orderItem.save()
    if orderItem.quantity <= 0:
        orderItem.delete()
    return JsonResponse('Item was added', safe=False)
#Checkouts by deleting all of the contents in the orderitem database and redirects the user back ot the main page being store.html
def process(request):
    OrderItem.objects.all().delete()
    return redirect('store')

def logout_view(request):
    logout(request)
    return redirect('store')

def login_view(request):
    login(request)
    return redirect('store')
