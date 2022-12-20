from django.urls import path
from Reviews import views

urlpatterns = [
    path("reviews", views.reviews, name="reviews")
]
