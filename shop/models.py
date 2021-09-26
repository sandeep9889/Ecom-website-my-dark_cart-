from django.db import models

# Create your models here.

class product(models.Model):
    
    product_id = models.AutoField
    product_name = models.CharField(max_length=50)
    desc = models.CharField(max_length=300, blank=True, null=True, )
     #herer we can put true for blank and null because vo push rha h ki age khali h usko empty rakhana h ki nahi kyu ki mene usko fill nahi kkra tha baad m
    pub_date = models.DateField(null=True,blank=True)
    def __str__(self):
        return self.product_name #here  we can make tittle as product name