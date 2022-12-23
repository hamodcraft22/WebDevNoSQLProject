from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth.decorators import login_required





from MoMaShop.models import Item, Comment, Order, OrderItem
from MoMaShop.forms import addItemForm, addCommentForm, addToOrderForm, checkoutForm
from MoMaShop.functions import handle_uploaded_file, addOrderItem

# Create your views here.
def home(request):
    return render(request, "MoMaShop/index.html")




def services(request, categoryid):
    service_Items = Item.objects.filter(category=categoryid)

    addToCartForm = addToOrderForm()
    if request.method == "POST" and "addToOrder" in request.POST:
        addToCartForm = addToOrderForm(request.POST)
        if addToCartForm.is_valid():

            itemID = request.POST["ItemID"]
            quantity = addToCartForm.cleaned_data["quantity"]

            addOrderItem(request=request,serviceId=itemID,quantity=quantity)
            return HttpResponseRedirect("/cart/")

    if request.method == "POST" and "removeItem" in request.POST:
        itemID = request.POST["ItemID"]

        itemDelete = Item.objects.get(id=itemID)
        itemDelete.delete()

    returned = {"service_Items":service_Items, "addToOrderForm":addToCartForm}
    return render(request, "MoMaShop/services.html", returned)



@login_required
def addService(request, categoryid):

    ItemForm = addItemForm()

    if request.method == "POST":
        ItemForm = addItemForm(request.POST, request.FILES)
        if ItemForm.is_valid():
            handle_uploaded_file(request.FILES['image'], categoryid)

            name = ItemForm.cleaned_data["name"]
            description = ItemForm.cleaned_data["description"]
            category = categoryid
            price = ItemForm.cleaned_data["price"]
            imageFileName = request.FILES['image'].name
            imagePath = "MoMaShop/img/{0}/{1}".format(category,imageFileName)

            itemObj = Item(name=name,description=description,category=category,price=price,image=imagePath)
            itemObj.save()

            return HttpResponseRedirect("/services/{}/".format(categoryid))



    return render(request, "MoMaShop/addService.html", {"ItemForm":ItemForm})



@login_required
def serviceDetails(request, serviceId):
    service_Item = Item.objects.get(id=serviceId)

    commentForm = addCommentForm()
    if request.method == "POST":
        commentForm = addCommentForm(request.POST)
        if commentForm.is_valid():

            user = request.user
            title = commentForm.cleaned_data["title"]
            body = commentForm.cleaned_data["body"]

            newComment = Comment(user=user,title=title,body=body,item=service_Item)
            newComment.save()

    allComments = Comment.objects.filter(item=serviceId)
    returned = {"service_Item":service_Item, "allComments":allComments, "commentForm":commentForm}

    return render(request, "MoMaShop/serviceDetails.html", returned)




@login_required
def cart(request):
    try:
        user = request.user

        customerOrder = Order.objects.get(user=user, ordererd="false")
        customerItems = customerOrder.items.all()

        actualItems = {}

        counter=0

        for item in customerItems:
            actualItems[item] = (customerItems[counter].item)
            counter += 1

        ## update item quantity
        if request.method == "POST" and "updateQty" in request.POST:

            orderItemID = request.POST["orderItemID"]
            quantity = request.POST["quantity"]

            orderItemUpdate = OrderItem.objects.get(id=orderItemID)
            orderItemUpdate.quantity = quantity
            orderItemUpdate.save()

            return HttpResponseRedirect("/cart")

        if request.method == "POST" and "removeOrderItem" in request.POST:
            orderItemID = request.POST["orderItemID"]

            orderItemDelete = OrderItem.objects.get(id=orderItemID)
            orderItemDelete.delete()

            return HttpResponseRedirect("/cart")

        returned = {"actualItems":actualItems, "customerItems":customerItems, "customerOrder":customerOrder}

        return render(request, "MoMaShop/cart.html", returned)
    except Order.DoesNotExist:
        return HttpResponse('you have no items in cart')



@login_required
def checkout(request):
    user = request.user
    customerOrder = Order.objects.get(user=user, ordererd="false")

    checkoutOrderForm = checkoutForm()
    if request.method == "POST":
        checkoutOrderForm = checkoutForm(request.POST)
        if checkoutOrderForm.is_valid():

            customerOrder.orderDate = datetime.datetime.now().date()
            customerOrder.paymentType = checkoutOrderForm.cleaned_data["paymentType"]
            customerOrder.cardNum = checkoutOrderForm.cleaned_data["cardNum"]
            customerOrder.cardExp = checkoutOrderForm.cleaned_data["cardExp"]
            customerOrder.comments = checkoutOrderForm.cleaned_data["comments"]
            customerOrder.ordererd = "true"

            customerOrder.save()

            return HttpResponseRedirect("/")

    return render(request, "MoMaShop/checkOut.html", {"checkoutOrderForm":checkoutOrderForm})
