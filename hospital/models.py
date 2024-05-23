from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Hospital(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    state = models.CharField(
        max_length=100, 
        choices=(
            ('Abuja', 'Abuja'), 
            ('Lagos', 'Lagos'), 
            ('Rivers', 'Rivers')
        )
    )
    country = models.CharField(
        max_length=100, 
        choices=(
            ('Nigeria', 'Nigeria'),
        )
    )
    is_available = models.BooleanField(default=True)

class Appointment(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    date = models.DateField()
    reason = models.CharField(max_length=255)
    status = models.CharField(
        max_length=20, 
        choices=(
            ('Scheduled', 'Scheduled'),
            ('Completed', 'Completed'),
            ('Cancelled', 'Cancelled')
        ), 
        null=True
    )


    
