from django.contrib.auth.models import User
from rest_framework import serializers
from products.models import Product
class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields=['product_name','product_code','category',
                'price','stock_quantity','image']
        read_only_fields=['id']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields=['username','email','password']

    def create(self, validated_data):
        u=User.objects.create_user(**validated_data)
        u.save()
        return u

