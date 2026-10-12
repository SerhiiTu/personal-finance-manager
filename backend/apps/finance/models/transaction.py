
from django.db import models

from apps.common.constants.currency import Currency
from apps.common.models import BaseModel
from apps.finance.constants.transaction import TransactionType
from apps.finance.models.account import Account
from apps.finance.models.category import Category
from apps.finance.models.context import Context
from apps.finance.models.subscription import Subscription
from apps.finance.models.scheduled_payment import ScheduledPayment
from apps.finance.models.transfer import Transfer
from apps.users.models import User


class Transaction(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transactions",
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="transactions",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="transactions",
    )

    context = models.ForeignKey(
        Context,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="transactions",
    )

    subscription = models.ForeignKey(
        Subscription,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="transactions",
    )

    scheduled_payment = models.ForeignKey(
        ScheduledPayment,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="transactions",
    )

    transfer = models.ForeignKey(
        Transfer,
        on_delete=models.PROTECT,
        null=True,
        blank=True,
        related_name="transactions",
    )

    type = models.CharField(
        max_length=10,
        choices=TransactionType.choices,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
    )

    transaction_date = models.DateTimeField()

    note = models.CharField(
        max_length=500,
        blank=True,
        default="",
    )

    class Meta:
        db_table = "transactions"

    def __str__(self):
        return f"{self.type}: {self.amount} {self.currency}"
