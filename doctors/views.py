from django.shortcuts import render
from .forms import DoctorForm
from django.contrib.auth.decorators import login_required
from accounts.decorators import allowed_users, admin_only, unauthenticated_user
from django.shortcuts import render, redirect, get_object_or_404
from .models import DoctorModel
from django.contrib import messages, auth
from .forms import DoctorForm
from patients.forms import SearchForm
from django.db.models import Q

# Create your views here.
def doctors(request):
    doctors = DoctorModel.objects.all().order_by('-date_joined')
    is_doctor = False
    search_form = SearchForm()
    if request.user.is_authenticated:
        is_doctor = DoctorModel.objects.filter(account=request.user).exists()

    return render(request, 'doctors/doctors_list.html', {'doctors' : doctors, 'is_doctor': is_doctor, 'search_form': search_form})




@login_required(login_url='login')
def doctor_profile(request):
    doctor = DoctorModel.objects.get(account=request.user)
    doctor_form = DoctorForm(instance=doctor)

    if request.method == 'POST':
        doctor_form = DoctorForm(request.POST, instance=doctor)
        if doctor_form.is_valid():
            doctor_form.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('dashboard')
        else: 
            redirect('dashboard')

    return render(request, 'doctors/doctor_profile.html', {'doctor_form': doctor_form, 'doctor': doctor})
    

@login_required(login_url='login')
def doctor_register(request):
    form = DoctorForm()
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            doctor = form.save(commit=False)
            doctor.account = request.user
            doctor.save()
            messages.success(request, 'Your profile has been updated.')
            return redirect('dashboard')
        else: 
            redirect('dashboard')
    else:
        form = DoctorForm()
    return render(request, 'doctors/doctor_register.html', {'form': form})


def search_view(request):
    search_form = SearchForm()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            doctors = DoctorModel.objects.order_by('-date_joined').filter(Q(account__first_name__icontains=keyword) | Q(designation__icontains=keyword) | Q(account__last_name__icontains=keyword) | Q(speciality__icontains=keyword) | Q(account__email__icontains=keyword))
            doctors_count = doctors.count()
    context = {
        'doctors': doctors,
        'd_count': doctors_count,
        'search_form': search_form,
    }
    return render(request, 'doctors/search_results.html', context) 


def doctor_details(request, doctor_id):
    doctor = get_object_or_404(DoctorModel, pk=doctor_id)
    return render(request, 'doctors/doctor_details.html', {'doctor': doctor})
