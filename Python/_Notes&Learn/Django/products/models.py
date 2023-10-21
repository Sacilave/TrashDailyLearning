from django.db import models
# 在这里创建模型


class Products(models.Model):
    name = models.CharField(max_length=255)
    prize = models.FloatField()
    stock = models.IntegerField()
    image_url = models.URLField(max_length=2083)
class Offer(models.Model):
    code = models.CharField(max_length=10)
    discrabe = models.CharField(max_length=255)
    discount = models.FloatField()
