# Generated by Django 3.0.8 on 2021-04-10 23:56

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeModel",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                ("address", models.TextField(null=True, unique=True, verbose_name="Dirección")),
                ("dni", models.CharField(max_length=16, unique=True, verbose_name="Cédula")),
                (
                    "phone_number",
                    models.CharField(max_length=25, null=True, verbose_name="Télefono"),
                ),
                (
                    "labor_specialty",
                    models.CharField(max_length=50, null=True, verbose_name="Especialidad"),
                ),
                (
                    "profile_photo",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="employees_photos",
                        verbose_name="Foto de Empleado",
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="employee",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "verbose_name": "Empleado",
                "verbose_name_plural": "Empleados",
                "ordering": ["id"],
            },
        ),
    ]
