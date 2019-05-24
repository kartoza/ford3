from django.db import models
from django.contrib.auth import get_user_model


class ProviderUsersCampusUsers(models.Model):
    provider_user_id = models.ForeignKey(
        get_user_model(),
        related_name='provider_user_id',
        null=True,
        on_delete=models.PROTECT)
    campus_user_id = models.ForeignKey(
        get_user_model(),
        related_name='campus_user_id',
        null=True,
        on_delete=models.PROTECT)
