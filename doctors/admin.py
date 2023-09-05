from django.contrib import admin
from .models import DoctorModel

class DoctorAdmin(admin.ModelAdmin):
    list_display = ('doctor_id','account', 'designation', 'speciality', 'experience', 'date_joined')
    
admin.site.register(DoctorModel, DoctorAdmin)