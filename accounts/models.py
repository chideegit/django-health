from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    email = models.EmailField(unique=True, null=False, blank=False)
    is_patient = models.BooleanField(default=False)
    is_doctor = models.BooleanField(default=False)

    has_patient_profile = models.BooleanField(default=False)
