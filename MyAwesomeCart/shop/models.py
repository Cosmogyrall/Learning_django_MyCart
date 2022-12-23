from django.db import models


# Create your models here.
class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    category = models.CharField(max_length=10, default='')
    pub_date = models.DateField(default='')
    price = models.IntegerField(default=0)
    subcategory = models.CharField(max_length=40, default='')
    image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.product_name
