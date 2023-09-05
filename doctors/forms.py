from django import forms
from . import models

class DoctorForm(forms.ModelForm):
    class Meta:
        model = models.DoctorModel
        fields = ('experience', 'designation', 'speciality', 'appointment_available_days')

    def __init__(self, *args, **kwargs):
        super(DoctorForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs['class'] = 'form-control'