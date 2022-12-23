from MoMaShop.models import Item, Order, OrderItem


## none view functions
def handle_uploaded_file(file, loc):
    with open('MoMaShop/static/MoMaShop/img/{0}/{1}'.format(loc,file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)




def addOrderItem(request, serviceId, quantity):
    # adding orderItem (many to many) to database
    serviceItem_ToAdd = Item.objects.get(id=serviceId)

    user = request.user

    #there is a present order
    if Order.objects.filter(user=user, ordererd="false"):
        presentOrder = Order.objects.get(user=user, ordererd="false")

        # the item is alredy present in the order
        if presentOrder.items.filter(item=serviceItem_ToAdd):
            presentItem = presentOrder.items.get(item=serviceItem_ToAdd)
            presentItem.quantity += quantity
            presentItem.save()
        else:
            # the item is new ti the order
            newOrderItem = OrderItem(user=user,item=serviceItem_ToAdd,quantity=quantity)
            newOrderItem.save()

            presentOrder.items.add(newOrderItem)
            presentOrder.save()
    else:
        # no order is found
        newOrder = Order(user=user)
        newOrder.save()

        newOrderItem = OrderItem(user=user,item=serviceItem_ToAdd,quantity=quantity)
        newOrderItem.save()

        newOrder.items.add(newOrderItem)
