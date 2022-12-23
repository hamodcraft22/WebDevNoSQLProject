from django.urls import path
from Users import views

urlpatterns = [
    path("accounts/register/", views.register, name='register')]
