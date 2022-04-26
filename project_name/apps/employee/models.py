from django.contrib.auth.models import User
from django.db import models


class EmployeeModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="employee")
    address = models.TextField(null=True, verbose_name="Dirección", unique=True)
    dni = models.CharField(max_length=16, verbose_name="Cédula", unique=True)
    phone_number = models.CharField(max_length=25, verbose_name="Télefono", null=True)
    labor_specialty = models.CharField(max_length=50, verbose_name="Especialidad", null=True)
    profile_photo = models.ImageField(
        null=True, upload_to="employees_photos", verbose_name="Foto de Empleado", blank=True
    )

    class Meta:
        verbose_name = "Empleado"
        verbose_name_plural = "Empleados"
        ordering = ["id"]
