from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    referral_code = models.CharField(max_length=10, blank=True, null=True)
    registration_timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username