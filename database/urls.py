from django.urls import path, include
from . import views
from django.views.generic.base import TemplateView 
from django.conf.urls.static import static
from django.conf import settings

#Webpages in the app
urlpatterns = [
    path("",views.store, name="store"),
    path("checkout/", views.checkout, name="checkout"),
    path("cart/", views.cart, name="cart"),
    path("update_item/", views.updateItem, name="update_item"),
    path("process/", views.process, name="process"),
    path("logout/", views.logout_view, name="logout"),
    path("login/", views.login_view, name="login")
]
#To initalize the media folder for images taken from settings.py
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)