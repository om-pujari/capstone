from django.db import models
from django.conf import settings

# Create your models here.
class Query(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    subject = models.CharField(max_length=255)
    message = models.TextField()
    response = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=50, choices=[('Open', 'Open'), ('Closed', 'Closed')], default='Open')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} - {self.user.name}"
