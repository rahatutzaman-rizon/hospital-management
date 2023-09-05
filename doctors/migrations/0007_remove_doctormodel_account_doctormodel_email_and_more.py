# Generated by Django 4.2.4 on 2023-09-02 16:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("doctors", "0006_remove_doctormodel_user_doctormodel_account"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="doctormodel",
            name="account",
        ),
        migrations.AddField(
            model_name="doctormodel",
            name="email",
            field=models.EmailField(default="example@mail.com", max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="doctormodel",
            name="fullname",
            field=models.CharField(default="fullname", max_length=255),
            preserve_default=False,
        ),
    ]