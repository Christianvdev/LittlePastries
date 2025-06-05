from django.db import models

# Create your models here.

class BakeryInfo(models.Model):
    BakeryName = models.CharField(max_length=64)
    BakeryDescription = models.TextField(default="")

    def __str__(self):
        return self.BakeryName
    

class Items(models.Model):
    FoodType = models.CharField(max_length=64)
    FoodPrice = models.DecimalField(decimal_places=2,max_digits=4 , default=0.00)

    def __str__(self):
        return self.FoodType
    
class ContactInfo(models.Model):
    contactNumber = models.CharField(max_length=25, default=123-456-7890)
    contactEmail = models.EmailField(max_length=64,default="test@gmail.com")

    def __str__(self):
        return self.contactEmail
