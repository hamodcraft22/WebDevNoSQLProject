from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect


from MoMaShop.models import Item, Comment, Order, OrderItem
from MoMaShop.forms import addItemForm, addCommentForm, addToOrderForm
from MoMaShop.functions import handle_uploaded_file, addOrderItem

# Create your views here.
def home(request):
    return render(request, "MoMaShop/index.html")




def services(request, categoryid):
    service_Items = Item.objects.filter(category=categoryid)

    addToCartForm = addToOrderForm()
    if request.method == "POST":
        addToCartForm = addToOrderForm(request.POST)
        if addToCartForm.is_valid():

            itemID = request.POST["ItemID"]
            quantity = addToCartForm.cleaned_data["quantity"]

            addOrderItem(request=request,serviceId=itemID,quantity=quantity)
            return HttpResponseRedirect("/cart/")


    returned = {"service_Items":service_Items, "addToOrderForm":addToCartForm}
    return render(request, "MoMaShop/services.html", returned)




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
