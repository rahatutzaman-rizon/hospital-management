from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from accounts.models import Account

class DoctorModel(models.Model):
    doctor_id = models.AutoField(primary_key=True)
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='doctor', null=True, blank=True)
    # account = models.OneToOneField(Account, on_delete=models.CASCADE, related_name='doctor', default=None)
    designation = models.CharField(max_length=255)
    speciality = models.CharField(max_length=255)
    experience = models.CharField(max_length=255)
    date_joined = models.DateTimeField(auto_now_add=True)

    # Appointment availability for multiple days
    APPOINTMENT_DAYS_CHOICES = [
        ('monday', 'Monday'),
        ('tuesday', 'Tuesday'),
        ('wednesday', 'Wednesday'),
        ('thursday', 'Thursday'),
        ('friday', 'Friday'),
        ('saturday', 'Saturday'),
        ('sunday', 'Sunday'),
    ]
    appointment_available_days = models.CharField(max_length=100, choices=APPOINTMENT_DAYS_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.account.first_name + " " + self.account.last_name + ' - ' + self.designation + ' - ' + self.speciality) 


