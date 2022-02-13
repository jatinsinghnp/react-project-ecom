from django.db import models

# Create your models here.


class Product(models.Model):
    product_title = models.CharField(max_length=200)
    product_desc = models.TextField()
    prod_img = models.ImageField(upload_to="products/photos", blank=True)

    def __str__(self):
        return self.product_title
