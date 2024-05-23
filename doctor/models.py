from django.db import models
from django.contrib.auth import get_user_model
from hospital.models import Hospital

User = get_user_model()

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    # other things 