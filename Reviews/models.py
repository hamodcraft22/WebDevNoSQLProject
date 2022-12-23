from django.db import models
from django.conf import settings


RATING_OPTIONS = (
("⭐","⭐"),
("⭐⭐","⭐⭐"),
("⭐⭐⭐","⭐⭐⭐"),
("⭐⭐⭐⭐","⭐⭐⭐⭐"),
("⭐⭐⭐⭐⭐","⭐⭐⭐⭐⭐"))

# Create your models here.
## site wide reviews
class Review(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.CharField(choices=RATING_OPTIONS, max_length=5) ## add limit
    description = models.TextField()
