from django.db import models

# Create your models here.
class Products(models.Model):
    name = models.CharField(max_length=100)
    image=models.FileField(upload_to='product_images/', null=True, blank=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()

    def __str__(self):
        return self.name