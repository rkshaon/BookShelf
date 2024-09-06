from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField(blank=True, null=True)  # Optional bio field
    birth_date = models.DateField(null=True, blank=True)
    died_date = models.DateField(null=True, blank=True)
    added_by = models.ForeignKey(
        'user_api.User',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )
    is_deleted = models.BooleanField(default=False)
    added_date_time = models.DateTimeField(auto_now_add=True)
    updated_date_time = models.DateTimeField(auto_now=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    @property
    def is_alive(self):
        return True if not self.died_date else False

    def __str__(self):
        return f'{self.first_name} {self.last_name}'
