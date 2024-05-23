from django import forms
from .models import *

class AddHospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class UpdateHospitalForm(forms.ModelForm):
    class Meta:
        model = Hospital
        fields = '__all__'

class BookAppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['date', 'reason']