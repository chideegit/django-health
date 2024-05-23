from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from .form import *
from .models import * 

def add_hospital(request):
    if request.method == 'POST':
        form = AddHospitalForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'New hospital added and saved to DB')
            return redirect('add-hospital')
        else:
            messages.warning(request, 'Something went wrong.')
            return redirect('add-hospital')
    else:
        form = AddHospitalForm()
        context = {'form':form}
    return render(request, 'hospital/add_hospital.html', context)

def update_hospital(request, pk):
    hospital = Hospital.objects.get(pk=pk)
    if request.method == 'POST':
        form = UpdateHospitalForm(request.POST, instance=hospital)
        if form.is_valid():
            form.save()
            messages.success(request, 'Hopsital info has been updated')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect(reverse('update-hospital', args=[hospital.pk]))
    else:
        form = UpdateHospitalForm(instance=hospital)
        context = {'form':form}
    return render(request, 'hospital/update_hospital.html', context)

def hospital_details(request, pk):
    hospital = Hospital.objects.get(pk=pk)
    context = {'hospital':hospital}
    return render(request, 'hospital/hospital_details.html', context)

def book_appointment(request, pk):
    hospital = Hospital.objects.get(pk=pk)
    if request.method == 'POST':
        form = BookAppointmentForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.patient = request.user
            var.hospital = hospital
            var.status = 'Scheduled'
            var.save()
            messages.success(request, 'Your profile and hospital has been paired')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('add-visit')
    else:
        form = BookAppointmentForm()
        context = {'form':form}
    return render(request, 'hospital/add_visit.html', context)
        