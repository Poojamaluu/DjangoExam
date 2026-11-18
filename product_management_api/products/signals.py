from django.contrib.auth.models import User
from django.db.models.signals import post_delete
from django.dispatch import receiver
from products.models import Product

@receiver(post_delete,sender=Product)
def show_message(sender,instance,**kwargs):

    print("Product is deleted")
