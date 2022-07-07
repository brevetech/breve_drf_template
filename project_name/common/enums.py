from django.db import models
from django.utils.translation import gettext_lazy as _


class PersonSexEnum(models.TextChoices):
    """Sex enum for Person Model"""

    MALE = "M", _("MALE")
    FEMALE = "F", _("FEMALE")
