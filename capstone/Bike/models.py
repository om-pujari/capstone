from django.db import models

# Create your models here.
class Bike(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    launch_date = models.DateField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    specifications = models.JSONField()  # Store specifications in key-value pairs
    image = models.ImageField(upload_to='bike_images/', blank=True, null=True)

    def __str__(self):
        return self.name

class Comparison(models.Model):
    bike_one = models.ForeignKey('Bike', on_delete=models.CASCADE, related_name='bike_one')
    bike_two = models.ForeignKey('Bike', on_delete=models.CASCADE, related_name='bike_two')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.bike_one.name} vs {self.bike_two.name}"
