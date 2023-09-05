from django.urls import path
from . import views


urlpatterns = [
    path('', views.patients, name='patients'),
    path('appointments/',views.appointments, name='appointments' ),
    path('create_appointment/', views.appointment_create_view, name='create_appointment'),
    path('search/', views.search_view, name='search_view'),
    path('appointments/<int:appointment_id>/edit/', views.edit_appointment, name='edit_appointment'),
    path('appointments/<int:appointment_id>/delete/', views.delete_appointment, name='delete_appointment'), 
]