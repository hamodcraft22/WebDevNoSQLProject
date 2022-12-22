from django.contrib import admin

# Register your models here.
from MoMaShop.models import Item, Order, Comment, OrderItem

admin.site.register(Item)
admin.site.register(Order)
admin.site.register(Comment)
admin.site.register(OrderItem)
