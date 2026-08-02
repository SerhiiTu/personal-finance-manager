from django.db import models

from apps.common.models import BaseModel
from apps.users.models import User


class Context(BaseModel):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="contexts",
    )

    name = models.CharField(
        max_length=255,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    color = models.CharField(
        max_length=7,
        blank=True,
        null=True,
    )

    icon = models.CharField(
        max_length=50,
        blank=True,
        null=True,
    )

    is_archived = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "contexts"
        ordering = ["name"]

    def __str__(self):
        return self.name