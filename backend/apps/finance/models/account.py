from decimal import Decimal

from django.db import models

from apps.common.constants.currency import Currency
from apps.common.models import BaseModel
from apps.finance.constants.account_type import AccountType
from apps.users.models import User


class Account(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="accounts",
    )

    name = models.CharField(
        max_length=255,
    )

    type = models.CharField(
        max_length=20,
        choices=AccountType.choices,
    )

    balance = models.DecimalField(
        max_digits=15,
        decimal_places=2,
        default=Decimal("0.00"),
    )

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.EUR,
    )

    color = models.CharField(
        max_length=7,
        blank=True,
        null=True,
    )

    icon = models.CharField(
        max_length=255,
        blank=True,
        null=True,
    )

    is_archived = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "accounts"
        ordering = ["name"]

    def __str__(self):
        return self.name