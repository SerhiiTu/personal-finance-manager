from django.db import models

class AccountType(models.TextChoices):
    CASH = "CASH", "Cash"
    CREDIT_CARD = "CREDIT_CARD", "Credit Card"
    DEBIT_CARD = "DEBIT_CARD", "Debit Card"