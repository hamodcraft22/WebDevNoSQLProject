from django.urls import path
from MoMaShop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/<int:id>/", views.services, name="services"),
    path("cart/", views.cart, name="cart")
]
