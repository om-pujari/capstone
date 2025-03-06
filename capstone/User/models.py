'''from django.contrib.auth.models import AbstractUser
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
            self.username = self.email  '''
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.core.validators import RegexValidator
from django.db import models
from Bike.models import Bike

class UserManager(BaseUserManager):
    def create_user(self, name, email=None, phone_number=None, password=None, **extra_fields):
        if not email and not phone_number:
            raise ValueError("Either email or phone number must be provided.")

        extra_fields.setdefault("is_active", True)

        user = self.model(
            email=self.normalize_email(email) if email else None,
            phone_number=phone_number,
            name=name,
            username=name,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, name, email, password=None, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        return self.create_user(name=name, email=email, password=password, **extra_fields)


class User(AbstractUser):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True, null=True, blank=True)
    phone_number = models.CharField(
        max_length=10,
        unique=True,
        null=True,
        blank=True,
        validators=[RegexValidator(regex=r'^[6-9]\d{9}$', message="Enter a valid 10-digit Indian phone number.")]
    )
    wishlist = models.ManyToManyField(Bike, blank=True, related_name='wishlisted_by')

    username = models.CharField(max_length=255, unique=True, blank=True, null=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    objects = UserManager()

    def save(self, *args, **kwargs):
        if not self.username:
            base_username = self.name.replace(" ", "").lower()
            counter = 1
            new_username = base_username

            # Fix the circular reference by using self.__class__
            while self.__class__.objects.filter(username=new_username).exclude(pk=self.pk).exists():
                counter += 1
                new_username = f"{base_username}{counter}"

            self.username = new_username

        super().save(*args, **kwargs)

    def __str__(self):
        return self.name
