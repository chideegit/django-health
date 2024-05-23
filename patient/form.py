from django import forms
from .models import *

class AddPatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('user', )

class UpdatePatientForm(forms.ModelForm):
    class Meta:
        model = Patient
        exclude = ('user', )

class AddEmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        exclude = ('patient', )
    
class UpdateEmergencyContactForm(forms.ModelForm):
    class Meta:
        model = EmergencyContact
        exclude = ('patient', )

class AddMedicalInfo(forms.ModelForm):
    class Meta:
        model = MedicalHistory
        exclude = ('patient', 'doctor')

class AddPrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = ('patient', 'doctor', 'timestamp')
        
class UpdatePrescriptionForm(forms.ModelForm):
    class Meta:
        model = Prescription
        exclude = ('patient', 'doctor', 'timestamp')