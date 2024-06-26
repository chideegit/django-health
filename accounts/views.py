from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from .form import * 
from patient.form import AddPatientForm

User = get_user_model()

def register_patient(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            var = form.save(commit=False)
            var.username = var.email
            var.is_patient = True
            var.save()
            messages.success(request, 'Your user account is now being created')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('register')
    else:
        form = RegisterUserForm()
        context = {'form':form}
    return render(request,  'accounts/register_patient.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None and user.is_active:
            login(request, user)
            messages.success(request, f'You are logged in as {user.email}')
            return redirect('dashboard')
        else:
            messages.warning(request, 'Something went wrong')
            return redirect('login')
    return render(request, 'accounts/login.html')

def logout_user(request):
    logout(request)
    messages.success(request, 'Your active session has ended')
    return redirect('login')
        
