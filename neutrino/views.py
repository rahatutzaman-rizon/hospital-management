from django.shortcuts import render
from doctors.models import DoctorModel
from patients.models import AppointmentModel
from patients.forms import SearchForm
from django.db.models import Q

def home(request):
    doctors = DoctorModel.objects.all().order_by('-date_joined')
    appointments = AppointmentModel.objects.all().order_by('-date')
    
    return render(request, "index.html", {'doctors': doctors, 'appointments': appointments})


