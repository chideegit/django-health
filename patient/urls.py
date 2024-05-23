from django.urls import path 
from .views import *

urlpatterns = [
    path('add-patient/', add_patient, name='add-patient'), 
    path('update-patient/<int:pk>/', update_patient, name='update-patient'), 
    path('add-emergency-contact', add_emergency_contact, name='add-emergency-contact'),
    path('update-emergency-contact/<int:pk>/', update_emergency_contact, name='update-emergency-contact'), 
    path('all-emergency-contacts/', all_emergency_contacts, name='all-emergency-contacts')
]