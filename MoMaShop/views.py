from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "MoMaShop/index.html")

def services(request, id):
    return render(request, "MoMaShop/services.html")

def cart(request):
    return render(request, "MoMaShop/cart.html")
