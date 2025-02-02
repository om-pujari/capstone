from django.contrib.auth.models import AbstractUser
from django.core.validators import RegexValidator
from django.db import models
from Bike.models import Bike

class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    wishlist = models.ManyToManyField(Bike, blank=True, related_name='wishlisted_by')
    phone_number = models.CharField(
        max_length=10,
        validators=[RegexValidator(
            regex=r'^[6-9]\d{9}$',
            message="Enter a valid 10-digit Indian phone number starting with 6-9."
        )],
        unique=True
    )

    # Use the default UserManager
    USERNAME_FIELD = 'email'  # Use email for login
    REQUIRED_FIELDS = ['username']  # Fields required on creation (besides email)

    def __str__(self):
        return self.name

    def clean(self):
        # Ensure username is set if required
        if not self.username:
            self.username = self.email
