from django.db import models


class FrequencyUnit(models.TextChoices):
    DAYS = "DAYS", "Days"
    WEEKS = "WEEKS", "Weeks"
    MONTHS = "MONTHS", "Months"
    YEARS = "YEARS", "Years"