from django.db import models

# Create your models here.
class Order(models.Model):
    order_id = models.CharField(max_length=100,unique=True)
    note = models.TextField(null=True,blank=True)
    total_order_amount = models.FloatField(default=0.0)
    customer_name = models.CharField(max_length=150,null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

