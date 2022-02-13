
from rest_framework import serializers
from shop.models import Product


class ProductSerilizers(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ["prod_img", "product_desc", "product_title"]
