from django.db import models


# class Publisher(models.Model):
#     name = models.CharField(max_length=255)
#     address = models.CharField(max_length=255, blank=True, null=True)
#     website = models.URLField(blank=True, null=True)
#     email = models.EmailField(blank=True, null=True)
#     phone_number = models.CharField(max_length=20, blank=True, null=True)
#     established_year = models.PositiveIntegerField(blank=True, null=True)
#     # Contact person at the publisher
#     contact_person = models.CharField(max_length=255, blank=True, null=True)
#     country = models.CharField(max_length=100, blank=True, null=True)
#     city = models.CharField(max_length=100, blank=True, null=True)

#     def __str__(self):
#         return self.name
