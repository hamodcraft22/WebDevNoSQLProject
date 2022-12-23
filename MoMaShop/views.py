from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from MoMaShop.models import Item, Comment, Order, OrderItem
from MoMaShop.forms import addItemForm, addCommentForm
from MoMaShop.uploadFile import handle_uploaded_file

# Create your views here.
def home(request):
    return render(request, "MoMaShop/index.html")




def services(request, categoryid):
    service_Items = Item.objects.filter(category=categoryid)
    return render(request, "MoMaShop/services.html", {"service_Items":service_Items})




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





def cart(request):
    return render(request, "MoMaShop/cart.html")





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

    # go to cart upon adding
    return HttpResponseRedirect("/cart/")
