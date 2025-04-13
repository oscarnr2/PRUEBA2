from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=200)
    descriptions = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    picture = models.ImageField(upload_to="django-ecommerce/")
    created_at = models.DateTimeField(auto_now_add=True)
    uptdated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
