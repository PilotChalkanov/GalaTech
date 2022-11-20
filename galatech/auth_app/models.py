from django.contrib.auth import models as auth_models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator
from django.db import models

from galatech.auth_app.common.validators import MaxFileSizeValidator
from galatech.auth_app.managers import GalatechUserManager


class GalatechUser(auth_models.AbstractBaseUser, auth_models.PermissionsMixin):
    USERNAME_MAX_LEN = 50
    USERNAME_MIN_LEN = 5
    email = models.EmailField(
        unique=True,
        null=False,
        blank=False
    )

    createdTimestamp = models.DateTimeField(
        auto_now_add=True
    )

    updatedTimestamp = models.DateTimeField(
        auto_now_add=True
    )

    is_staff = models.BooleanField(
        default=False,
    )

    USERNAME_FIELD = 'email'

    objects = GalatechUserManager()

class Ticket(models.Model):

    MAX_LEN_ASSIGNMENT = 5
    MIN_LEN_ASSIGNMENT = 25

    NORMAL = 'Normal'
    PRIORITY = 'Priority'
    URGENT = 'Urgent'
    CRITICAL = 'Critical'

    TYPES = [(x,x) for x in (NORMAL, PRIORITY, URGENT, CRITICAL)]

    STATUS_CHOICES = [
        ('TODO', 'TODO'),
        ('IN PROGRESS', 'IN PROGRESS'),
        ('IN REVIEW', 'IN REVIEW'),
        ('DONE', 'DONE'),
    ]

    title = models.CharField(
        max_length=MAX_LEN_ASSIGNMENT,
        validators=(
            MinLengthValidator(MIN_LEN_ASSIGNMENT),
                    )
    )

    type = models.CharField(
        max_length=max(len(x) for x,_ in TYPES),
        choices=TYPES,
        default='Normal',
    )
    status = models.CharField('Status',
                              choices=STATUS_CHOICES,
                              default='TODO',
                              max_length=255,
                              blank=True,
                              null=True)

    photo = models.ImageField(
        validators=(
            MaxFileSizeValidator(5),
                    )
    )

    description = models.TextField(
        max_length=500,
        validators=(
            MinLengthValidator(MIN_LEN_ASSIGNMENT),
        )
    )


