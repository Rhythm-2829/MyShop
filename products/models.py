from django.db import models

# Create your models here.
class Shirt(models.Model):
    # id = models.AutoField()
    title = models.CharField(max_length = 70)
    price = models.PositiveIntegerField() 
    brand = models.CharField(max_length = 70, null=True)
    description = models.TextField(blank=True)
    is_bestseller = models.BooleanField(default=False)


    def __str__(self):
        return f"{self.title}"


class Producct(models.Model):
    title=models.CharField(max_length=70)
    description = models.TextField(blank=True)
    Category = models.CharField(max_length=100)
    Image = models.ImageField(blank=True)
    Brand=models.CharField(max_length=50)
    Price=models.PositiveIntegerField()
    def __str__(self):
        return f"{self.title}"








    
