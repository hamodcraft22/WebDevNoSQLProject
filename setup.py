from MoMaShop.models import Item

item1 = Item(name="Basic Image", description="No Characters Included\r\n1080p Resolution", category="si", price=5, image="MoMaShop/img/si/basicStillImage.png")
item2 = Item(name="Normal Image", description="2 Characters Included\r\n2k Resolution", category="si", price=25, image="MoMaShop/img/si/normalStillImage.png")
item3 = Item(name="Fancy Image", description="Customized Characters\r\n8k Resolution", category="si", price=80, image="MoMaShop/img/si/fancyStillImage.png")
item1.save()
item2.save()
item3.save()

item4 = Item(name="Basic Gif", description="10 seconds\r\n1080p Resolution", category="ai", price=15, image="MoMaShop/img/ai/basicAnimatedImage.gif")
item5 = Item(name="Normal Gif", description="20 seconds\r\n2k Resolution", category="ai", price=35, image="MoMaShop/img/ai/normalAnimatedImage.gif")
item6 = Item(name="Fancy Gif", description="30 seconds\r\n8k Resolution", category="ai", price=70, image="MoMaShop/img/ai/fancyAnimatedImage.gif")
item4.save()
item5.save()
item6.save()

item7 = Item(name="Short Video", description="~1 minute\r\n1080p Resolution", category="cv", price=50, image="MoMaShop/img/cv/basicVideo.gif")
item8 = Item(name="Normal Video", description="~ 5 minutes\r\n2k Resolution", category="cv", price=100, image="MoMaShop/img/cv/normalVideo.gif")
item9 = Item(name="Fancy Video", description="~15 minutes\r\n8k Resolution", category="cv", price=200, image="MoMaShop/img/cv/fancyVideo.gif")
item7.save()
item8.save()
item9.save()
