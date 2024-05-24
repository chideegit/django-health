from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    if request.user.is_patient:
        return render(request, 'dashboard/patient_dashboard.html')
    elif request.user.is_doctor:
        return render(request, 'dashboard/doctor_dashboard.html')
    else:
        return render(request, 'dashboard/dashboard.html')