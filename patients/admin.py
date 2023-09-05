from django.contrib import admin
from .models import AppointmentModel

class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('id','patient_name', 'patient_contact', 'patient_age', 'doctor', 'date', 'time', 'is_new', 'appointment_time', 'disease_syndrome')
    
admin.site.register(AppointmentModel, AppointmentAdmin)