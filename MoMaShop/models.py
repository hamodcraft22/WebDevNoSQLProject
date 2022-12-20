from django.db import models
from django.conf import settings

CATEGORY_CHOICES = (
    ('SI', 'Still Image'),
    ('AI', 'Animated Image'),
    ('CV', 'Customized Video')
)

PAYMENT_CHOICES = (
    ('CC', 'Credit Card'),
    ('DC', 'Debit Card')
)
##fix these


##create functions for all of these
# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    category = models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    price = models.FloatField()
    image = models.CharField(max_length=100)


class OrderItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def getPrice(self):
        return self.quantity * self.item.price


class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField(OrderItem)
    startDate = models.DateTimeField(auto_now_add=True)
    orderDate = models.DateTimeField()
    paymentType = models.CharField(choices=PAYMENT_CHOICES, max_length=2)
    cardNum = models.IntegerField()
    cardExp = models.DateField()
    comments = models.TextField()
    ordererd = models.BooleanField(default=False)

    def getTotal(self):
        total = 0
        for orderItem in self.items.all():
            total += orderItem.getPrice()
        return total


class Comment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    createdOn = models.DateTimeField(auto_now_add=True)
    item = models.ForeignKey(Item,on_delete=models.CASCADE)