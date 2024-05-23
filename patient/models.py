from django.db import models
from django.contrib.auth import get_user_model
from hospital.models import Appointment

User = get_user_model()

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    dob = models.DateField()
    gender = models.CharField(
        max_length=15, 
        choices=(
            ('Male', 'Male'), 
            ('Female', 'Female')
        )
    )
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
    phone_number = models.CharField(max_length=20)

class EmergencyContact(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    full_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100)
    email_address = models.EmailField(max_length=100)

class MedicalHistory(models.Model):
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    diagnosis = models.CharField(max_length=255)
    treatment = models.CharField(max_length=255)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    doctor_note = models.CharField(max_length=200)
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctorss')

class Prescription(models.Model):
    doctor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='doctors')
    patient = models.ForeignKey(User, on_delete=models.CASCADE)
    appointment = models.ForeignKey(Appointment, on_delete=models.CASCADE)
    dosage = models.TextField()
    comments = models.CharField(max_length=100, null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    
