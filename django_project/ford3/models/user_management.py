from django.db import models
from django.contrib.auth.models import User


class ProvinceUserManagementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__groups__id=1)


class ProviderUserManagementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__groups__id=3)


class CampusUserManagementManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(user__groups__id=2)


class UserManagement(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    email_confirmed = models.BooleanField(default=False)

    objects = models.Manager()
    province_objects = ProvinceUserManagementManager()
    provider_objects = ProviderUserManagementManager()
    campus_objects = CampusUserManagementManager()
