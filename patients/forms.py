from django import forms
from .models import AppointmentModel

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = AppointmentModel
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['patient_name'].widget.attrs['placeholder'] = 'Enter Patient Name'
        self.fields['patient_age'].widget.attrs['placeholder'] = 'Enter Patient Age'
        self.fields['patient_contact'].widget.attrs['placeholder'] = 'Enter Phone No. / Email'
        self.fields['date'].widget.attrs['placeholder'] = 'Enter Date'
        self.fields['time'].widget.attrs['placeholder'] = 'Enter Time'
        self.fields['disease_syndrome'].widget.attrs['placeholder'] = 'Enter Disease/Syndrome'

        for field in self.fields:  
            if field != 'is_new':
                self.fields[field].widget.attrs['class'] = 'form-control'


class SearchForm(forms.Form):
    keyword = forms.CharField(label='Search', max_length=100)