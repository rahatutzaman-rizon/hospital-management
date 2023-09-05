from django.shortcuts import render, redirect, get_object_or_404
from .models import AppointmentModel
from .forms import AppointmentForm, SearchForm
from django.contrib.auth.decorators import login_required
from doctors.models import DoctorModel
from django.db.models import Q

# Create your views here.
@login_required
def patients(request):
    search_form = SearchForm()
    doctor = DoctorModel.objects.get(account=request.user)  
    patients = doctor.appointment.all().order_by('-date')
    print(patients)
    return render(request, 'patients.html', {'appointments': patients, 'search_form': search_form})

def appointments(request):
    appointments = AppointmentModel.objects.all().order_by('-appointment_time') 
    return render(request, 'appoinments.html', {'appointments': appointments})


@login_required(login_url='login')
def appointment_create_view(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data)
            form.save()
            return redirect('appointments') 
    else:
        form = AppointmentForm()
        print('something error')

    return render(request, 'appointment_form.html', {'form': form})


def search_view(request):
    search_form = SearchForm()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            patients = AppointmentModel.objects.order_by('-date').filter(Q(patient_name__icontains=keyword) | Q(doctor__designation__icontains=keyword) | Q(disease_syndrome__icontains=keyword) | Q(doctor__speciality__icontains=keyword) | Q(doctor__account__first_name__icontains=keyword) | Q(doctor__account__last_name__icontains=keyword))
            patients_count = patients.count()
    context = {
        'patients': patients,
        'p_count': patients_count,
        'search_form': search_form,
    }
    return render(request, 'search_results.html', context) 


def edit_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentModel, pk=appointment_id)
    
    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()
            return redirect('appointments')  
    else:
        form = AppointmentForm(instance=appointment)

    return render(request, 'edit_appointment.html', {'form': form})

def delete_appointment(request, appointment_id):
    appointment = get_object_or_404(AppointmentModel, pk=appointment_id)

    if request.method == 'POST':
        appointment.delete()
        return redirect('appointments')

    return render(request, 'delete_appointment.html', {'appointment': appointment})