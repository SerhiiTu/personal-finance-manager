
from django.db import models

from apps.common.models import BaseModel
from apps.finance.models.account import Account
from apps.users.models import User


class Transfer(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="transfers",
    )

    from_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="outgoing_transfers",
    )

    to_account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="incoming_transfers",
    )

    from_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    to_amount = models.DecimalField(
        max_digits=12,
        decimal_places=2,
    )

    fee = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0,
    )

    exchange_rate = models.DecimalField(
        max_digits=18,
        decimal_places=8,
        default=1,
    )

    transfer_date = models.DateTimeField()

    note = models.CharField(
        max_length=500,
        blank=True,
        default="",
    )

    class Meta:
        db_table = "transfers"

    def __str__(self):
        return (
            f"Transfer: {self.from_amount} "
            f"from account {self.from_account_id} "
            f"to {self.to_amount} "
            f"to account {self.to_account_id}"
        )
