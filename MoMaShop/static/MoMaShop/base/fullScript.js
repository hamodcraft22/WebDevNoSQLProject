/*Global variables*/

/*Retrive Current Order Items(Qty) from session storage*/
var basicStillImageQty = sessionStorage.getItem('basicStillImageQty');
var normalStillImageQty = sessionStorage.getItem('normalStillImageQty');
var fancyStillImageQty = sessionStorage.getItem('fancyStillImageQty');
var basicAnimatedImageQty = sessionStorage.getItem('basicAnimatedImageQty');
var normalAnimatedImageQty = sessionStorage.getItem('normalAnimatedImageQty');
var fancyAnimatedImageQty = sessionStorage.getItem('fancyAnimatedImageQty');
var basicVideoQty = sessionStorage.getItem('basicVideoQty');
var normalVideoQty = sessionStorage.getItem('normalVideoQty');
var fancyVideoQty = sessionStorage.getItem('fancyVideoQty');
/*End Retrive Current Order Items(Qty) from session storage*/


/*Retrive Last Order Items(Qty) from local storage*/
var basicStillImageOrderQty = localStorage.getItem('basicStillImageQty');
var normalStillImageOrderQty = localStorage.getItem('normalStillImageQty');
var fancyStillImageOrderQty = localStorage.getItem('fancyStillImageQty');
var basicAnimatedImageOrderQty = localStorage.getItem('basicAnimatedImageQty');
var normalAnimatedImageOrderQty = localStorage.getItem('normalAnimatedImageQty');
var fancyAnimatedImageOrderQty = localStorage.getItem('fancyAnimatedImageQty');
var basicVideoOrderQty = localStorage.getItem('basicVideoQty');
var normalVideoOrderQty = localStorage.getItem('normalVideoQty');
var fancyVideoOrderQty = localStorage.getItem('fancyVideoQty');
/*End Retrive Last Order Items(Qty) from local storage*/


/*Calculate Individual items Totals Per item For currnt orders*/
var basicStillImageTotal = (basicStillImageQty*5);
var normalStillImageTotal = (normalStillImageQty*25);
var fancyStillImageTotal = (fancyStillImageQty*80);
var basicAnimatedImageTotal = (basicAnimatedImageQty*15);
var normalAnimatedImageTotal = (normalAnimatedImageQty*35);
var fancyAnimatedImageTotal = (fancyAnimatedImageQty*70);
var basicVideoTotal = (basicVideoQty*50);
var normalVideoTotal = (normalVideoQty*100);
var fancyVideoTotal = (fancyVideoQty*200);

var totalCartPrice = (basicStillImageTotal+normalStillImageTotal+fancyStillImageTotal+basicAnimatedImageTotal+normalAnimatedImageTotal+fancyAnimatedImageTotal+basicVideoTotal+normalVideoTotal+fancyVideoTotal);
/*End Calculate Individual items Totals Per item For currnt orders*/


/*Calculate Individual items Totals Per item For past orders*/
var basicStillImageOrderTotal = (basicStillImageOrderQty*5);
var normalStillImageOrderTotal = (normalStillImageOrderQty*25);
var fancyStillImageOrderTotal = (fancyStillImageOrderQty*80);
var basicAnimatedImageOrderTotal = (basicAnimatedImageOrderQty*15);
var normalAnimatedImageOrderTotal = (normalAnimatedImageOrderQty*35);
var fancyAnimatedImageOrderTotal = (fancyAnimatedImageOrderQty*70);
var basicVideoOrderTotal = (basicVideoOrderQty*50);
var normalVideoOrderTotal = (normalVideoOrderQty*100);
var fancyVideoOrderTotal = (fancyVideoOrderQty*200);

var userOrderTotal = (basicStillImageOrderTotal+normalStillImageOrderTotal+fancyStillImageOrderTotal+basicAnimatedImageOrderTotal+normalAnimatedImageOrderTotal+fancyAnimatedImageOrderTotal+basicVideoOrderTotal+normalVideoOrderTotal+fancyVideoOrderTotal);
/*End Calculate Individual items Totals Per item For past orders*/


/*Check if there is a past order from local storage*/
var hasPrevousOrder = localStorage.getItem('hasPrevousOrder');
/*End Check if there is a past order from local storage*/


/*check if cart has items*/
function cartCheck()
{

  if (totalCartPrice == 0)
  {
    document.getElementById('emptyCartCont').style.display = "block";
    document.getElementById('checkoutCartNav').setAttribute("onclick", "cartEmptyAlert()" );
  }
  else
  {
    document.getElementById('checkoutCartNav').href = "payment.html";
    displayTotal();
  }
}
/*End check if cart has items*/


/*check if the use has prevous orders*/
function prevOrderCheck()
{
  if (hasPrevousOrder === null)
  {
    document.getElementById('prevOrderNav').setAttribute("onclick", "noPrevOrderAlert()" );
  }
  else
  {
    document.getElementById('prevOrderNav').href = "lastOrder.html";
  }
}
/*End check if the use has prevous orders*/


/*alert user of empty cart on checkout*/
function cartEmptyAlert()
{
  alert("Your cart is empty, Add services before checking out");
}
/*End alert user of empty cart on checkout*/


/*alert user of no prevous orders*/
function noPrevOrderAlert()
{
  alert("No Past Orders Were Found For You");
}
/*End alert user of no prevous orders*/


/*show the total of cart in nav bar*/
function displayTotal()
{
  document.getElementById('totalCartNav').innerHTML = ("Total: "+ totalCartPrice+ " BHD");
}
/*End show the total of cart in nav bar*/


/*Refresh/display all Quantities for current orders*/
function qtyTotalRefresh()
{
  qtyRefresh_Images();
  qtyRefresh_Gifs();
  qtyRefresh_Vids();

  TotalRefresh_Images();
  TotalRefresh_Gifs();
  TotalRefresh_Vids();
}
/*End Refresh/display all Quantities for current orders*/


/*Refresh/display still images Quantities for current orders*/
function qtyRefresh_Images()
{
  document.getElementById('basicStillImageQty').value = basicStillImageQty;
  document.getElementById('normalStillImageQty').value = normalStillImageQty;
  document.getElementById('fancyStillImageQty').value = fancyStillImageQty;
}
/*End Refresh/display still images Quantities for current orders*/


/*Refresh/display Animated images Quantities for current orders*/
function qtyRefresh_Gifs()
{
  document.getElementById('basicAnimatedImageQty').value = basicAnimatedImageQty;
  document.getElementById('normalAnimatedImageQty').value = normalAnimatedImageQty;
  document.getElementById('fancyAnimatedImageQty').value = fancyAnimatedImageQty;
}
/*End Refresh/display Animated images Quantities for current orders*/

/*Refresh/display videos Quantities for current orders*/
function qtyRefresh_Vids()
{
  document.getElementById('basicVideoQty').value = basicVideoQty;
  document.getElementById('normalVideoQty').value = normalVideoQty;
  document.getElementById('fancyVideoQty').value = fancyVideoQty;
}
/*End Refresh/display videos Quantitiesv for current orders*/


/*Refresh/display still images Totals for current orders*/
function TotalRefresh_Images()
{
  document.getElementById('basicStillImageTotal').innerHTML = basicStillImageTotal+" BHD";
  document.getElementById('normalStillImageTotal').innerHTML = normalStillImageTotal+" BHD";
  document.getElementById('fancyStillImageTotal').innerHTML = fancyStillImageTotal+" BHD";
}
/*End Refresh/display still images Totals for current orders*/


/*Refresh/display Animated images Totals for current orders*/
function TotalRefresh_Gifs()
{
  document.getElementById('basicAnimatedImageTotal').innerHTML = basicAnimatedImageTotal+" BHD";
  document.getElementById('normalAnimatedImageTotal').innerHTML = normalAnimatedImageTotal+" BHD";
  document.getElementById('fancyAnimatedImageTotal').innerHTML = fancyAnimatedImageTotal+" BHD";
}
/*End Refresh/display Animated images Totals for current orders*/


/*Refresh/display Videos Totals for current orders*/
function TotalRefresh_Vids()
{
  document.getElementById('basicVideoTotal').innerHTML = basicVideoTotal+" BHD";
  document.getElementById('normalVideoTotal').innerHTML = normalVideoTotal+" BHD";
  document.getElementById('fancyVideoTotal').innerHTML = fancyVideoTotal+" BHD";
}
/*End Refresh Videos Totals for current orders*/

/*Refresh/display Videos Totals for past orders*/
function OrderQtyTotal()
{
  document.getElementById('basicStillImageQty').innerHTML = basicStillImageOrderQty;
  document.getElementById('normalStillImageQty').innerHTML = normalStillImageOrderQty;
  document.getElementById('fancyStillImageQty').innerHTML = fancyStillImageOrderQty;
  document.getElementById('basicAnimatedImageQty').innerHTML = basicAnimatedImageOrderQty;
  document.getElementById('normalAnimatedImageQty').innerHTML = normalAnimatedImageOrderQty;
  document.getElementById('fancyAnimatedImageQty').innerHTML = fancyAnimatedImageOrderQty;
  document.getElementById('basicVideoQty').innerHTML = basicVideoOrderQty;
  document.getElementById('normalVideoQty').innerHTML = normalVideoOrderQty;
  document.getElementById('fancyVideoQty').innerHTML = fancyVideoOrderQty;


  document.getElementById('basicStillImageTotal').innerHTML = basicStillImageOrderTotal+" BHD";
  document.getElementById('normalStillImageTotal').innerHTML = normalStillImageOrderTotal+" BHD";
  document.getElementById('fancyStillImageTotal').innerHTML = fancyStillImageOrderTotal+" BHD";
  document.getElementById('basicAnimatedImageTotal').innerHTML = basicAnimatedImageOrderTotal+" BHD";
  document.getElementById('normalAnimatedImageTotal').innerHTML = normalAnimatedImageOrderTotal+" BHD";
  document.getElementById('fancyAnimatedImageTotal').innerHTML = fancyAnimatedImageOrderTotal+" BHD";
  document.getElementById('basicVideoTotal').innerHTML = basicVideoOrderTotal+" BHD";
  document.getElementById('normalVideoTotal').innerHTML = normalVideoOrderTotal+" BHD";
  document.getElementById('fancyVideoTotal').innerHTML = fancyVideoOrderTotal+" BHD";
}
/*End Refresh/display Videos Totals for past orders*/


/*Display spisific product/item if added for currnt orders*/
function cartItemsDisplay()
{
  if (basicStillImageTotal != 0)
  {
      document.getElementById('basicStillImage').style.display = "inline-block";
  }
  if (normalStillImageTotal != 0)
  {
      document.getElementById('normalStillImage').style.display = "inline-block";
  }
  if (fancyStillImageTotal != 0)
  {
      document.getElementById('fancyStillImage').style.display = "inline-block";
  }
  if (basicAnimatedImageTotal != 0)
  {
      document.getElementById('basicAnimatedImage').style.display = "inline-block";
  }
  if (normalAnimatedImageTotal != 0)
  {
      document.getElementById('normalAnimatedImage').style.display = "inline-block";
  }
  if (fancyAnimatedImageTotal != 0)
  {
      document.getElementById('fancyAnimatedImage').style.display = "inline-block";
  }
  if (basicVideoTotal != 0)
  {
      document.getElementById('basicVideo').style.display = "inline-block";
  }
  if (normalVideoTotal != 0)
  {
      document.getElementById('normalVideo').style.display = "inline-block";
  }
  if (fancyVideoTotal != 0)
  {
      document.getElementById('fancyVideo').style.display = "inline-block";
  }
}
/*End Display spisific product/item if added for currnt orders*/


/*Display spisific product/item if added for past orders*/
function OrderItemsDisplay()
{
  if (basicStillImageOrderTotal != 0)
  {
      document.getElementById('basicStillImage').style.display = "inline-block";
  }
  if (normalStillImageOrderTotal != 0)
  {
      document.getElementById('normalStillImage').style.display = "inline-block";
  }
  if (fancyStillImageOrderTotal != 0)
  {
      document.getElementById('fancyStillImage').style.display = "inline-block";
  }
  if (basicAnimatedImageOrderTotal != 0)
  {
      document.getElementById('basicAnimatedImage').style.display = "inline-block";
  }
  if (normalAnimatedImageOrderTotal != 0)
  {
      document.getElementById('normalAnimatedImage').style.display = "inline-block";
  }
  if (fancyAnimatedImageOrderTotal != 0)
  {
      document.getElementById('fancyAnimatedImage').style.display = "inline-block";
  }
  if (basicVideoOrderTotal != 0)
  {
      document.getElementById('basicVideo').style.display = "inline-block";
  }
  if (normalVideoOrderTotal != 0)
  {
      document.getElementById('normalVideo').style.display = "inline-block";
  }
  if (fancyVideoOrderTotal != 0)
  {
      document.getElementById('fancyVideo').style.display = "inline-block";
  }
}
/*End Display spisific product/item if added for past orders*/



/*Add item to cart*/
function basicStillImageCart()
{
  var basicStillImageQty = document.getElementById('basicStillImageQty').value;
  sessionStorage.setItem('basicStillImageQty',basicStillImageQty);
  alert(basicStillImageQty + " Basic Still Images have been added to your cart");
}

function normalStillImageCart()
{
  var normalStillImageQty = document.getElementById('normalStillImageQty').value;
  sessionStorage.setItem('normalStillImageQty',normalStillImageQty);
  alert(normalStillImageQty + " Normal Still Images have been added to your cart");
}

function fancyStillImageCart()
{
  var fancyStillImageQty = document.getElementById('fancyStillImageQty').value;
  sessionStorage.setItem('fancyStillImageQty',fancyStillImageQty);
  alert(fancyStillImageQty + " 🌟Fancy✨ Still Images have been added to your cart");
}


function basicAnimatedImageCart()
{
  var basicAnimatedImageQty = document.getElementById('basicAnimatedImageQty').value;
  sessionStorage.setItem('basicAnimatedImageQty',basicAnimatedImageQty);
  alert(basicAnimatedImageQty + " Basic Animated Images have been added to your cart");
}

function normalAnimatedImageCart()
{
  var normalAnimatedImageQty = document.getElementById('normalAnimatedImageQty').value;
  sessionStorage.setItem('normalAnimatedImageQty',normalAnimatedImageQty);
  alert(normalAnimatedImageQty + " Normal Animated Images have been added to your cart");
}

function fancyAnimatedImageCart()
{
  var fancyAnimatedImageQty = document.getElementById('fancyAnimatedImageQty').value;
  sessionStorage.setItem('fancyAnimatedImageQty',fancyAnimatedImageQty);
  alert(fancyAnimatedImageQty + " 🌟Fancy✨ Animated Images have been added to your cart");
}


function basicVideoCart()
{
  var basicVideoQty = document.getElementById('basicVideoQty').value;
  sessionStorage.setItem('basicVideoQty',basicVideoQty);
  alert(basicVideoQty + " Basic Videos have been added to your cart");
}

function normalVideoCart()
{
  var normalVideoQty = document.getElementById('normalVideoQty').value;
  sessionStorage.setItem('normalVideoQty',normalVideoQty);
  alert(normalVideoQty + " Normal Videos have been added to your cart");
}

function fancyVideoCart()
{
  var fancyVideoQty = document.getElementById('fancyVideoQty').value;
  sessionStorage.setItem('fancyVideoQty',fancyVideoQty);
  alert(fancyVideoQty + " 🌟Fancy✨ Videos have been added to your cart");
}
/*End Add item to cart*/


/*change in cart item Quantity*/
function basicStillImageUpdate()
{
  var basicStillImageQty = document.getElementById('basicStillImageQty').value;
  sessionStorage.setItem('basicStillImageQty',basicStillImageQty);
  alert(basicStillImageQty + " Basic Still Images Quantity have been updated");
}

function normalStillImageUpdate()
{
  var normalStillImageQty = document.getElementById('normalStillImageQty').value;
  sessionStorage.setItem('normalStillImageQty',normalStillImageQty);
  alert(normalStillImageQty + " Normal Still Images Quantity have been updated");
}

function fancyStillImageUpdate()
{
  var fancyStillImageQty = document.getElementById('fancyStillImageQty').value;
  sessionStorage.setItem('fancyStillImageQty',fancyStillImageQty);
  alert(fancyStillImageQty + " 🌟Fancy✨ Still Images Quantity have been updated");
}


function basicAnimatedImageUpdate()
{
  var basicAnimatedImageQty = document.getElementById('basicAnimatedImageQty').value;
  sessionStorage.setItem('basicAnimatedImageQty',basicAnimatedImageQty);
  alert(basicAnimatedImageQty + " Basic Animated Images Quantity have been updated");
}

function normalAnimatedImageUpdate()
{
  var normalAnimatedImageQty = document.getElementById('normalAnimatedImageQty').value;
  sessionStorage.setItem('normalAnimatedImageQty',normalAnimatedImageQty);
  alert(normalAnimatedImageQty + " Normal Animated Images Quantity have been updated");
}

function fancyAnimatedImageUpdate()
{
  var fancyAnimatedImageQty = document.getElementById('fancyAnimatedImageQty').value;
  sessionStorage.setItem('fancyAnimatedImageQty',fancyAnimatedImageQty);
  alert(fancyAnimatedImageQty + " 🌟Fancy✨ Animated Images Quantity have been updated");
}


function basicVideoUpdate()
{
  var basicVideoQty = document.getElementById('basicVideoQty').value;
  sessionStorage.setItem('basicVideoQty',basicVideoQty);
  alert(basicVideoQty + " Basic Videos Quantity have been updated");
}

function normalVideoUpdate()
{
  var normalVideoQty = document.getElementById('normalVideoQty').value;
  sessionStorage.setItem('normalVideoQty',normalVideoQty);
  alert(normalVideoQty + " Normal Videos Quantity have been updated");
}

function fancyVideoUpdate()
{
  var fancyVideoQty = document.getElementById('fancyVideoQty').value;
  sessionStorage.setItem('fancyVideoQty',fancyVideoQty);
  alert(fancyVideoQty + " 🌟Fancy✨ Videos Quantity have been updated");
}
/*End change in cart item Quantity*/


/*delete in cart item*/
function basicStillImageDelete()
{
  sessionStorage.removeItem('basicStillImageQty')
  alert("Basic Still Images have been removed from your cart");
}

function normalStillImageDelete()
{
  sessionStorage.removeItem('normalStillImageQty');
  alert("Normal Still Images have been removed from your cart");
}

function fancyStillImageDelete()
{
  sessionStorage.removeItem('fancyStillImageQty');
  alert("🌟Fancy✨ Still images have been removed from your cart");
}


function basicAnimatedImageDelete()
{
  sessionStorage.removeItem('basicAnimatedImageQty');
  alert("Basic Animated Images have been removed from your cart");
}

function normalAnimatedImageDelete()
{
  sessionStorage.removeItem('normalAnimatedImageQty');
  alert("Normal Animated Images have been removed from your cart");
}

function fancyAnimatedImageDelete()
{
  sessionStorage.removeItem('fancyAnimatedImageQty');
  alert("🌟Fancy✨ Animated Images have been removed from your cart");
}


function basicVideoDelete()
{
  sessionStorage.removeItem('basicVideoQty');
  alert("Basic Videos have been removed from your cart");
}

function normalVideoDelete()
{
  sessionStorage.removeItem('normalVideoQty');
  alert("Normal Videos have been removed from your cart");
}

function fancyVideoDelete()
{
  sessionStorage.removeItem('fancyVideoQty');
  alert("🌟Fancy✨ Videos have been removed from your cart");
}
/*delete in cart item*/


/*Confirm and save order + details to local storage*/
function confirmOrder()
{

  /*to remove any past orders that wernt deleted properly*/
  localStorage.removeItem('basicStillImageQty');
  localStorage.removeItem('normalStillImageQty');
  localStorage.removeItem('fancyStillImageQty');
  localStorage.removeItem('basicAnimatedImageQty');
  localStorage.removeItem('normalAnimatedImageQty');
  localStorage.removeItem('fancyAnimatedImageQty');
  localStorage.removeItem('basicVideoQty');
  localStorage.removeItem('normalVideoQty');
  localStorage.removeItem('fancyVideoQty');


  /*to check if an item has been aded to the cart and add it to confirmOrder*/
  if (basicStillImageQty != null)
  {
    localStorage.setItem('basicStillImageQty',basicStillImageQty);
  }

  if (normalStillImageQty != null)
  {
    localStorage.setItem('normalStillImageQty',normalStillImageQty);
  }

  if (fancyStillImageQty != null)
  {
   localStorage.setItem('fancyStillImageQty',fancyStillImageQty);
  }

  if (basicAnimatedImageQty != null)
  {
    localStorage.setItem('basicAnimatedImageQty',basicAnimatedImageQty);
  }

  if (normalAnimatedImageQty != null)
  {
    localStorage.setItem('normalAnimatedImageQty',normalAnimatedImageQty);
  }

  if (fancyAnimatedImageQty != null)
  {
    localStorage.setItem('fancyAnimatedImageQty',fancyAnimatedImageQty);
  }

  if (basicVideoQty != null)
  {
    localStorage.setItem('basicVideoQty',basicVideoQty);
  }

  if (normalVideoQty != null)
  {
    localStorage.setItem('normalVideoQty',normalVideoQty);
  }

  if (fancyVideoQty != null)
  {
    localStorage.setItem('fancyVideoQty',fancyVideoQty);
  }

  /*retrive inputed user information for order details*/
  var userOrderNameInput = document.getElementById('userOrderNameInput').value;
  var userOrderCommentInput = document.getElementById('userOrderCommentInput').value;
  var userOrderFullCardInput = document.getElementById('userCardNumberInput').value;
  var userPaymentOption = document.getElementsByName('userPaymentOption').id;
  var dateOSys = new Date();
  var dateOfOrder = dateOSys.getFullYear()+'-'+(dateOSys.getMonth()+1)+'-'+dateOSys.getDate();


  /*save inputed user information for order details*/
  localStorage.setItem('userOrderNameInput',userOrderNameInput);
  localStorage.setItem('userOrderCommentInput',userOrderCommentInput);
  localStorage.setItem('userOrderTotal', totalCartPrice);
  localStorage.setItem('userOrderDate', dateOfOrder);

  if (userPaymentOption == "debetCardCheck")
  {
    localStorage.setItem('userPaymentOption',"Debet Card");
  }
  else
  {
    localStorage.setItem('userPaymentOption',"Credit Card");
  }

  var userOrderFullCardString = userOrderFullCardInput.toString();
  var userOrderLastCardDigits = userOrderFullCardString.substring(12);

  localStorage.setItem('userOrderLastCardDigits', "************"+userOrderLastCardDigits);

  localStorage.setItem('hasPrevousOrder', "yes");


  /*remove confirmed order from cart*/
  sessionStorage.removeItem('basicStillImageQty');
  sessionStorage.removeItem('normalStillImageQty');
  sessionStorage.removeItem('fancyStillImageQty');
  sessionStorage.removeItem('basicAnimatedImageQty');
  sessionStorage.removeItem('normalAnimatedImageQty');
  sessionStorage.removeItem('fancyAnimatedImageQty');
  sessionStorage.removeItem('basicVideoQty');
  sessionStorage.removeItem('normalVideoQty');
  sessionStorage.removeItem('fancyVideoQty');

  /*alert user and move to last order page*/
  alert ("Your Order Has Been Placed!!!, You will be diracted to your Order Details");
  window.open("lastOrder.html","_self");
}
/*End Confirm and save order + details to local storage*/


/*display order details in last order page*/
function orderDetails()
{
  var userOrderNameInput = localStorage.getItem('userOrderNameInput');
  var userOrderDate = localStorage.getItem('userOrderDate');
  var userOrderTotal = localStorage.getItem('userOrderTotal');
  var userOrderCommentInput = localStorage.getItem('userOrderCommentInput');
  var userCardNumber = localStorage.getItem('userOrderLastCardDigits');
  var userPaymentOption = localStorage.getItem('userPaymentOption');

  document.getElementById('userOrderNameInput').innerHTML = userOrderNameInput;
  document.getElementById('userOrderDate').innerHTML = userOrderDate;
  document.getElementById('userOrderTotal').innerHTML = userOrderTotal+" BHD";
  document.getElementById('userOrderCommentInput').innerHTML = userOrderCommentInput;
  document.getElementById('userCardNumber').innerHTML = userCardNumber;
  document.getElementById('userPaymentOption').innerHTML = userPaymentOption;
}
/*End display order details in last order page*/


/*submit / save an order in local storage*/
function userReviewSubmitFunc()
{
  var userReviewNamevar = document.getElementById('userReviewNameinput').value;
  var userReviewReviewvar = document.getElementById('userReviewReviewinput').value;
  var userReviewRatingvar = document.getElementById('userReviewRatinginput').value;

  /*to display rating in stars*/
  if (userReviewRatingvar == 1)
  {
      var userReviewRatingStarvar = "⭐";
  }
  else if (userReviewRatingvar == 2)
  {
    var userReviewRatingStarvar = "⭐⭐";
  }
  else if (userReviewRatingvar == 3)
  {
    var userReviewRatingStarvar = "⭐⭐⭐";
  }
  else if (userReviewRatingvar == 4)
  {
  var userReviewRatingStarvar = "⭐⭐⭐⭐";
  }
  else if (userReviewRatingvar == 5)
  {
    var userReviewRatingStarvar = "⭐⭐⭐⭐⭐";
  }

  localStorage.setItem('userReviewNameinput', userReviewNamevar);
  localStorage.setItem('userReviewRatinginput', userReviewRatingvar);
  localStorage.setItem('userReviewReviewinput', userReviewReviewvar);
  localStorage.setItem('userReviewSatrinput', userReviewRatingStarvar);
}
/*End submit / save an order in local storage*/


/*display user review if avalible*/
function userReviewcheckFunc()
{
  if ("userReviewNameinput" in localStorage)
  {
    document.getElementById('userReview').style.display = "block";
    var userReviewNamevar = localStorage.getItem('userReviewNameinput');
    var userReviewRatingvar = localStorage.getItem('userReviewRatinginput');
    var userReviewStarvar = localStorage.getItem('userReviewSatrinput');
    var userReviewReviewvar = localStorage.getItem('userReviewReviewinput');

    document.getElementById('nameOfUser').innerHTML = userReviewNamevar;
    document.getElementById('ratingOfUser').innerHTML = userReviewStarvar;
    document.getElementById('reviewOfUser').innerHTML = userReviewReviewvar;

    document.getElementById('userReviewNameinput').value = userReviewNamevar;
    document.getElementById('userReviewRatinginput').value = userReviewRatingvar;
    document.getElementById('userReviewReviewinput').value = userReviewReviewvar;
    document.getElementById('reviewStat').innerHTML = "Modify Your Review:";
    document.getElementById('inputButton').value = "Modify";
    }
  else
  {
    document.getElementById('userReview').style.display = "none";
    document.getElementById('deleteButton').style.display = "none";
    document.getElementById('reviewStat').innerHTML = "Write Your Review:";
  }
}
/*End display user review if avalible*/

/*delete the user review*/
function userReviewDeleteFunc()
{
  localStorage.removeItem('userReviewNameinput');
  localStorage.removeItem('userReviewRatinginput');
  localStorage.removeItem('userReviewReviewinput');
}
/*End delete the user review*/
