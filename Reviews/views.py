from django.shortcuts import render
from Reviews.forms import reviewForm
from Reviews.models import Review
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect

# Create your views here.
@login_required
def reviews(request):
    allReviews = Review.objects.all

    addToReviewsForm = reviewForm()
    if request.method == "POST":
        addToReviewsForm = reviewForm(request.POST)
        if addToReviewsForm.is_valid():

            user = request.user
            rating = addToReviewsForm.cleaned_data["rating"]
            description = addToReviewsForm.cleaned_data["description"]

            newReview = Review(user=user, rating=rating, description=description)
            newReview.save()

            return HttpResponseRedirect("/reviews")

    return render(request, "Reviews/reviews.html", {"addToReviewsForm":addToReviewsForm, "allReviews":allReviews})
