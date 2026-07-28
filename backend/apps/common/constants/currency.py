from django.db import models


class Currency(models.TextChoices):
    EUR = "EUR", "Euro"
    USD = "USD", "US Dollar"
    UAH = "UAH", "Ukrainian Hryvnia"
    CZK = "CZK", "Czech Koruna"