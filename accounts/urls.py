from django.urls import path 
from .views import *

urlpatterns = [
    path('register-patient/', register_patient, name='register-patient'), 
    path('login/', login_user, name='login'), 
    path('logout/', logout_user, name='logout')
]