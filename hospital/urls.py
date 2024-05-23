from django.urls import path
from .views import *

urlpatterns = [
    path('add-hospital/', add_hospital, name='add-hospital'), 
    path('update-hospital/<int:pk>/', update_hospital, name='update-hospital'), 
    path('hospital-details/<int:pk>/', hospital_details, name='hospital-details'), 
    path('book-appointment/', book_appointment, name='add-visit')
]