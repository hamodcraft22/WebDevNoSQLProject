from django.db import models

# Create your models here.
class TestObj(models.Model):
    name=models.TextField()
    desc=models.TextField()


class OtherTest(models.Model):
    name=models.CharField(max_length=100)
