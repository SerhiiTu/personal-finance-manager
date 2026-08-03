from django.db import models


class CategoryType(models.TextChoices):
    EXPENSE = "EXPENSE", "Expense"
    INCOME = "INCOME", "Income"