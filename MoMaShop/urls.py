from django.urls import path
from MoMaShop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/<str:categoryid>/", views.services, name="services"),
    path("addService/<str:categoryid>/", views.addService, name="addService"),
    path("serviceDetails/<int:serviceId>/", views.serviceDetails, name="serviceDetails"),
    path("cart/", views.cart, name="cart"),
    path("addOrderItem/<int:serviceId>/", views.addOrderItem, name="addOrderItem")
]
