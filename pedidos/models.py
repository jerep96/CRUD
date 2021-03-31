from django.db import models
from login.models import *
from productos.models import *


# Create your models here.
class Order (models.Model):
    id_client = models.ForeignKey(Client, on_delete=models.CASCADE)
    id_product = models.ForeignKey(Product, on_delete=models.CASCADE)
    bought_products = models.IntegerField('bought', default=0)

