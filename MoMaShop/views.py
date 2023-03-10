from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import datetime
from django.contrib.auth.decorators import login_required





from MoMaShop.models import Item, Comment, Order, OrderItem
from MoMaShop.forms import addItemForm, addCommentForm, addToOrderForm, checkoutForm
from MoMaShop.functions import handle_uploaded_file, addOrderItem

# Create your views here.

# home view
def home(request):
    return render(request, "MoMaShop/index.html")



# service (products) page
def services(request, categoryid):
    # collect all items with the correct ctageory id (for a spisifc page)
    service_Items = Item.objects.filter(category=categoryid)

    # create an instance of the add to cart form
    addToCartForm = addToOrderForm()

    # if the add to cart button was pressed
    if request.method == "POST" and "addToOrder" in request.POST:
        addToCartForm = addToOrderForm(request.POST)
        if addToCartForm.is_valid():

            # spicy method of getting information from html page, hidden input in a form that gets the data from the spisifc object in the html page
            itemID = request.POST["ItemID"]
            quantity = addToCartForm.cleaned_data["quantity"]

            addOrderItem(request=request,serviceId=itemID,quantity=quantity)
            return HttpResponseRedirect("/cart/")

    # if the super user clicks on the remove button
    if request.method == "POST" and "removeItem" in request.POST:
        itemID = request.POST["ItemID"]

        itemDelete = Item.objects.get(id=itemID)
        itemDelete.delete()

    returned = {"service_Items":service_Items, "addToOrderForm":addToCartForm}
    return render(request, "MoMaShop/services.html", returned)

# edit service (product / item) page, made seprat to include picture, not made using form as custome formating is being used (again becuse of using MongoDB)
def editService(request, serviceId):
    service_Item = Item.objects.get(id=serviceId)

    # if the user clickes update
    if request.method == "POST":

        # get all the items (categories of user)
        name = request.POST["name"]
        description = request.POST["description"]
        category = request.POST["categoryid"]
        price = request.POST["price"]


        # update the new information
        service_Item.name = name
        service_Item.description = description
        service_Item.category = category
        service_Item.price = price

        # if the user updated the image
        if len(request.FILES) != 0:
            # do the whole upload image process
            imageFileName = request.FILES['image'].name # get image name
            imagePath = "MoMaShop/img/{0}/{1}".format(category,imageFileName) # manifast an image path (to save to mongoDB)

            handle_uploaded_file(request.FILES['image'], category) # pass the image to the upload file method
            service_Item.image = imagePath # finally update the image in the db

        # save all the updates
        service_Item.save()

        return HttpResponseRedirect("/services/{}/".format(category))


    return render(request, "MoMaShop/editService.html", {"service_Item":service_Item})


# add new service (product) to the store, has to be logged in
@login_required
def addService(request, categoryid):

    # create an instance of the add item form
    ItemForm = addItemForm()

    # if the submit button is clicked
    if request.method == "POST":
        # get the actual request + the item submited (image)
        ItemForm = addItemForm(request.POST, request.FILES)
        if ItemForm.is_valid():
            # call the upload button function while passing the actual file and the category (for the path)
            handle_uploaded_file(request.FILES['image'], categoryid)

            name = ItemForm.cleaned_data["name"]
            description = ItemForm.cleaned_data["description"]
            category = categoryid
            price = ItemForm.cleaned_data["price"]
            imageFileName = request.FILES['image'].name
            imagePath = "MoMaShop/img/{0}/{1}".format(category,imageFileName)

            # create a new item and save it in the database (djongo MongoDB)
            itemObj = Item(name=name,description=description,category=category,price=price,image=imagePath)
            itemObj.save()

            return HttpResponseRedirect("/services/{}/".format(categoryid))



    return render(request, "MoMaShop/addService.html", {"ItemForm":ItemForm})


# view details / comment on services
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



# cart view function
@login_required
def cart(request):
    # exception handler, display a cart empty message if the cart is empty
    try:
        # get the current user
        user = request.user

        # check if the user has a current order, if it DoesNotExist it will throw a not found exception - extra challanging work ????
        customerOrder = Order.objects.get(user=user, ordererd="false")
        customerItems = customerOrder.items.all()

        actualItems = {}

        counter=0

        # retrive the actual items (products) of the order - requiried since its using a many to many field and it dosent return an actual object
        for item in customerItems:
            actualItems[item] = (customerItems[counter].item)
            counter += 1


        ## update item quantity function - user can update quantity within cart
        if request.method == "POST" and "updateQty" in request.POST:

            orderItemID = request.POST["orderItemID"]
            quantity = request.POST["quantity"]

            orderItemUpdate = OrderItem.objects.get(id=orderItemID)
            orderItemUpdate.quantity = quantity
            orderItemUpdate.save()

            return HttpResponseRedirect("/cart")

        # remove item from cart
        if request.method == "POST" and "removeOrderItem" in request.POST:
            orderItemID = request.POST["orderItemID"]

            orderItemDelete = OrderItem.objects.get(id=orderItemID)
            orderItemDelete.delete()

            return HttpResponseRedirect("/cart")

        returned = {"actualItems":actualItems, "customerItems":customerItems, "customerOrder":customerOrder}

        return render(request, "MoMaShop/cart.html", returned)
    except Order.DoesNotExist:
        return HttpResponse('you have no items in cart')


# checkout - set order status as true - as ordered
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
