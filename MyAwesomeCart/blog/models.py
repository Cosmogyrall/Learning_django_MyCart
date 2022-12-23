from django.db import models


# Create your models here.
class Blogpost(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=20)
    desc = models.CharField(max_length=50)
    category = models.CharField(max_length=10, default='')
    pub_date = models.DateField(default='')
    price = models.IntegerField(default=0)
    subcategory = models.CharField(max_length=40, default='')
    #image = models.ImageField(upload_to='shop/images', default='')

    def __str__(self):
        return self.product_name
