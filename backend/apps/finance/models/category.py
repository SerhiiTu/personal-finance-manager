from django.db import models

from apps.common.models import BaseModel
from apps.finance.constants.category import CategoryType
from apps.users.models import User


class Category(BaseModel):
    name = models.CharField(
        max_length=255,
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="categories",
    )

    is_default = models.BooleanField(
        default=False,
    )

    parent_category = models.ForeignKey(
        "self",
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="children",
    )

    type = models.CharField(
        max_length=20,
        choices=CategoryType.choices,
    )

    color = models.CharField(
        max_length=7,
        null=True,
        blank=True,
    )

    icon = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    is_archived = models.BooleanField(
        default=False,
    )

    class Meta:
        db_table = "categories"

    def __str__(self):
        return self.name