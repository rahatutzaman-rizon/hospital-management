# Generated by Django 4.2.4 on 2023-09-03 06:55

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("patients", "0006_alter_appointmentmodel_patient_contact"),
    ]

    operations = [
        migrations.DeleteModel(
            name="PatientModel",
        ),
    ]