from django.db import models

from apps.common.constants.currency import Currency
from apps.common.constants.frequency import FrequencyUnit
from apps.common.models import BaseModel
from apps.finance.constants.subscription import SubscriptionStatus
from apps.finance.models.account import Account
from apps.finance.models.category import Category
from apps.finance.models.context import Context
from apps.users.models import User


class Subscription(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="subscriptions",
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="subscriptions",
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.PROTECT,
        related_name="subscriptions",
    )

    context = models.ForeignKey(
        Context,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="subscriptions",
    )

    name = models.CharField(
        max_length=255,
    )

    amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
    )

    frequency_unit = models.CharField(
        max_length=10,
        choices=FrequencyUnit.choices,
    )

    frequency_interval = models.PositiveIntegerField(
        default=1,
    )

    provider_url = models.URLField(
        max_length=255,
        null=True,
        blank=True,
    )

    next_payment_date = models.DateField()

    start_date = models.DateField()

    end_date = models.DateField(
        null=True,
        blank=True,
    )

    status = models.CharField(
        max_length=20,
        choices=SubscriptionStatus.choices,
        default=SubscriptionStatus.ACTIVE,
    )

    class Meta:
        db_table = "subscriptions"

    def __str__(self):
        return self.name