from django.db import models


# Create your models here.
class Supplier (models.Model):
    company_name = models.CharField('Company name', max_length=50, help_text="Name of the supplier company")
    company_line = models.CharField('Company line', max_length=50, help_text="Company line")

    def __str__(self):
        return str(self.company_name)


class Product (models.Model):
    id_supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    product_name = models.CharField('Product name', max_length=50, help_text="Product name")
    product_description = models.TextField('product Description', max_length=200, help_text="Product description")
    stock_product = models.IntegerField('Stock', default=0)
    product_price = models.DecimalField('Price', decimal_places=2, max_digits=10, default=0)

    def __str__(self):
        return str(self.id)





