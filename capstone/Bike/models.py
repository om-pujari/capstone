from django.db import models
from django.conf import settings

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

class ServiceType(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return f"{self.name} - ₹{self.price}"

class Maintenance(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    service_type = models.ForeignKey(ServiceType, on_delete=models.CASCADE)
    service_date = models.DateField(null=True, blank=True)
    comments = models.TextField(blank=True, null=True)
    status = models.CharField(
        max_length=50,
        choices=[("Pending", "Pending"), ("Completed", "Completed"), ('Canceled', 'Canceled'),],
        default="Pending"
    )
    class Meta:
        verbose_name_plural = "Maintenance Requests"

    def __str__(self):
        return f"{self.bike.name} - {self.service_type.name} ({self.get_status_display()})"



class Review(models.Model):
    bike = models.ForeignKey('Bike', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=[(i, i) for i in range(1, 6)])
    text = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Review for {self.bike.name} by {self.user.username}"