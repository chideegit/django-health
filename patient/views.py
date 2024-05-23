from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import get_user_model
from .models import * 
from .form import *

User = get_user_model()

def add_patient(request):
    if request.method == 'POST':
        form = AddPatientForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.user = request.user
            get_user = User.objects.get(pk=request.user.pk)
            get_user.has_patient_profile = True
            var.save()
            get_user.save()
            messages.success(request, 'Your profile is now complete')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('add-patient')
    else:
        form = AddPatientForm()
        context = {'form':form}
    return render(request, 'patient/add_patient.html', context)


def update_patient(request, pk):
    patient = Patient.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdatePatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated and saved')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect(reverse('update-patient', args=[patient.pk]))
    else:
        form = UpdatePatientForm(instance=patient)
        context = {'form':form}
    return render(request, 'patient/update_patient.html', context)

def add_emergency_contact(request):
    if request.method == 'POST':
        form = AddEmergencyContactForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.patient = request.user
            var.save()
            messages.success(request, 'New Emergency contact saved')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('add-emergency-contact')
    else:
        form = AddEmergencyContactForm()
        context = {'form':form}
    return render(request, 'patient/add_emergency_contact.html', context)

def update_emergency_contact(request, pk):
    contact = EmergencyContact.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateEmergencyContactForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            messages.success(request, 'Emergency contact information is now updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect(reverse('update-emergency-contact', args=[contact.pk]))
    else:
        form = UpdateEmergencyContactForm(instance=contact)
        context = {'form':form}
    return render(request, 'patient/update_emergency_contact.html', context)

def all_emergency_contacts(request):
    contacts = EmergencyContact.objects.filter(patient=request.user)
    context = {'contacts':contacts}
    return render(request, 'patient/all_emergency_contacts.html', context)