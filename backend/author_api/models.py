from django.db import models
from django.utils.translation import gettext_lazy as _


class Author(models.Model):
    first_name = models.CharField(
        _('First Name'),
        max_length=100,
        blank=True,
        null=True
    )
    middle_name = models.CharField(
        _('Middle Name'),
        max_length=100,
        blank=True,
        null=True
    )
    last_name = models.CharField(
        _('Last Name'),
        max_length=100,
        blank=True,
        null=True
    )
    biography = models.TextField(blank=True, null=True)
    birth_date = models.DateField(
        _('Birth Date'),
        null=True,
        blank=True
    )
    died_date = models.DateField(
        _('Died Date'),
        null=True,
        blank=True
    )
    added_by = models.ForeignKey(
        'user_api.User',
        related_name='added_authors',
        verbose_name=_('Added By'),
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(
        _('Added Date Time'),
        auto_now_add=True
    )
    updated_date_time = models.DateTimeField(
        _('Updated Date Time'),
        auto_now=True
    )

    @property
    def full_name(self):
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

    @property
    def is_alive(self):
        return True if not self.died_date else False

    def __str__(self):
        return f'{self.full_name}'
