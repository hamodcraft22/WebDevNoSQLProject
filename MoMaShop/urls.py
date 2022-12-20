from django.urls import path
from MoMaShop import views

urlpatterns = [
    path("", views.homePage, name="homePage")
]
