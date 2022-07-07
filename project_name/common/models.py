from django.db import models

# https://stackoverflow.com/questions/1737017/django-auto-now-and-auto-now-add/1737078#1737078
from project_name.common.enums import PersonSexEnum


class TimeStampedModel(models.Model):
    """
    Defines a timestamped model with create_date (auto_now_add) and update_date (auto_now)
    """

    create_date = models.DateField(
        auto_now_add=True, editable=False, verbose_name="Fecha de creación"
    )
    update_date = models.DateField(
        auto_now=True, editable=False, verbose_name="Última modificación"
    )

    class Meta:
        abstract = True


class PersonModel(TimeStampedModel):
    """Defines a generic representation of a person data model"""

    first_name = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Primer Nombre"
    )
    second_name = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Segundo Nombre"
    )
    first_surname = models.CharField(
        max_length=50, null=False, blank=False, verbose_name="Primer Apellido"
    )
    second_surname = models.CharField(
        max_length=50, null=True, blank=True, verbose_name="Segundo Apellido"
    )
    address = models.TextField(null=False, blank=False, verbose_name="Dirección")
    id_number = models.CharField(
        max_length=16,
        verbose_name="Cédula",
        unique=True,
        null=False,
        blank=False,
    )
    birthdate = models.DateField(null=False, blank=False, verbose_name="Fecha de Nacimiento")
    phone = models.CharField(max_length=25, verbose_name="Télefono", null=True, blank=True)
    email = models.EmailField(
        max_length=50, null=True, blank=True, verbose_name="Correo Electrónico"
    )
    sex = models.CharField(
        max_length=1,
        null=False,
        blank=False,
        verbose_name="Sexo",
        choices=PersonSexEnum.choices,
        default=PersonSexEnum.FEMALE,
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"{self.first_name} {self.second_name} {self.first_surname} {self.second_surname}"
