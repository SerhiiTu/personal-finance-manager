from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.db import models

from apps.common.models import BaseModel
from apps.users.managers import UserManager

from apps.common.constants.currency import Currency


class User(BaseModel, AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(
        unique=True,
        max_length=255,
    )

    first_name = models.CharField(
        max_length=255,
    )

    last_name = models.CharField(
        max_length=255,
    )

    avatar_path = models.CharField(
        max_length=255,
        null=True,
        blank=True,
    )

    default_currency = models.CharField(
        max_length=3,
        choices=Currency.choices,
        default=Currency.EUR,
    )

    timezone = models.CharField(
        max_length=50,
        default="UTC",
    )

    is_active = models.BooleanField(
        default=True,
    )

    is_staff = models.BooleanField(
        default=False,
    )

    email_verified_at = models.DateTimeField(
        null=True,
        blank=True,
    )

    objects = UserManager()

    USERNAME_FIELD = "email"

    REQUIRED_FIELDS = [
        "first_name",
        "last_name",
    ]

    class Meta:
        db_table = "users"

    def __str__(self):
        return self.email