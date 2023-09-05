from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from accounts.models import Account
from doctors.models import DoctorModel
   


class AppointmentModel(models.Model):
    patient_name = models.CharField(max_length=255)
    patient_contact = models.CharField(max_length=255)
    patient_age = models.IntegerField()
    doctor = models.ForeignKey(DoctorModel, on_delete=models.CASCADE, related_name='appointment')
    date = models.DateField()
    time = models.TimeField()
    disease_syndrome = models.CharField(max_length=255, null=True, blank=True)
    is_new = models.BooleanField(default=True)
    appointment_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment for {self.patient_name} with Dr. {self.doctor.designation} on {self.date} at {self.time}"
