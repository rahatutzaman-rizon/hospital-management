from django.urls import path
from . import views


urlpatterns = [
    path('', views.doctors, name='doctors'),
    path('doctor_profile/', views.doctor_profile, name='doctor_profile'),
    path('', views.doctor_register, name='doctor_register'),
    path('search/', views.search_view, name='search_doctors'),
    path('details/<int:doctor_id>/', views.doctor_details, name='doctor_details'),
]