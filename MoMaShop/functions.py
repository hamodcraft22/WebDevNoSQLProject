from MoMaShop.models import Item, Order, OrderItem


## none view functions

# a file upload function - i should copyright this - not found online as mongoDB dosent save files - shared with students of the class
def handle_uploaded_file(file, loc):
    with open('MoMaShop/static/MoMaShop/img/{0}/{1}'.format(loc,file.name), 'wb+') as destination:
        for chunk in file.chunks():
            destination.write(chunk)



# add items to cart "current order"
def addOrderItem(request, serviceId, quantity):
    # adding orderItem (many to many) to database
    serviceItem_ToAdd = Item.objects.get(id=serviceId)

    user = request.user

    #there is a present order - just add or edit the item
    if Order.objects.filter(user=user, ordererd="false"):
        presentOrder = Order.objects.get(user=user, ordererd="false")

        # the item is alredy present in the order (add the quantity to present quantity)
        if presentOrder.items.filter(item=serviceItem_ToAdd):
            presentItem = presentOrder.items.get(item=serviceItem_ToAdd)
            presentItem.quantity += quantity
            presentItem.save()
        else:
            # the item is new to the order
            newOrderItem = OrderItem(user=user,item=serviceItem_ToAdd,quantity=quantity)
            newOrderItem.save()

            presentOrder.items.add(newOrderItem)
            presentOrder.save()
    else:
        # no order is found - create new order and add item
        newOrder = Order(user=user)
        newOrder.save()

        newOrderItem = OrderItem(user=user,item=serviceItem_ToAdd,quantity=quantity)
        newOrderItem.save()

        newOrder.items.add(newOrderItem)
