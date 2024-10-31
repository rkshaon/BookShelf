from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

import os

from BookShelf.utilities.storage import ReplaceExistingFileStorage


replace_existing_file_storage = ReplaceExistingFileStorage()


def profile_upload_path(instance, filename):
    """
    Generates a unique file path
    and renames the file with the User ID.
    """
    ext = filename.split('.')[-1]
    new_filename = f"{instance.id}.{ext}"

    return os.path.join('profile', new_filename)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('The Email field must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(email, password, **extra_fields)


class User(AbstractUser):
    ROLE_CHOICES = (
        (1, 'Admin'),
        (2, 'Moderator'),
        (3, 'Reader'),
    )

    first_name = models.CharField(
        max_length=255, blank=True, null=True
    )
    middle_name = models.CharField(
        max_length=255, blank=True, null=True
    )
    last_name = models.CharField(
        max_length=255, blank=True, null=True
    )
    email = models.EmailField(unique=True)
    username = models.CharField(
        max_length=50,
        unique=True,
        blank=True,
        null=True)  # Optional username
    role = models.PositiveIntegerField(choices=ROLE_CHOICES, default=3)
    profile_image = models.ImageField(
        upload_to=profile_upload_path,
        blank=True,
        null=True,
        storage=replace_existing_file_storage
    )
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'role']

    @property
    def full_name(self) -> str:
        name = ""

        if self.first_name:
            name += f"{self.first_name}"

        if self.middle_name:
            if name:
                name += f" {self.middle_name}"
            else:
                name += f"{self.middle_name}"

        if self.last_name:
            if name:
                name += f" {self.last_name}"
            else:
                name += f"{self.last_name}"

        return name

    def __str__(self):
        return self.full_name
