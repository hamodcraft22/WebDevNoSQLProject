from django.urls import path
from MoMaShop import views

urlpatterns = [
    path("", views.home, name="home"),
    path("services/<str:categoryid>/", views.services, name="services"),
    path("addService/<str:categoryid>/", views.addService, name="addService"),
    path("editService/<int:serviceId>/", views.editService, name="editService"),
    path("serviceDetails/<int:serviceId>/", views.serviceDetails, name="serviceDetails"),
    path("cart/", views.cart, name="cart"),
    path("checkout/", views.checkout, name="checkout")
]
