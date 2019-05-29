from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from ford3.models.user import User, ProvinceUser
from ford3.notifier import Notifier


def send_activation_email(sender, instance, created, **kwargs):
    if created:
        Notifier.send_activation_email(instance)


def add_user_to_group(sender, instance, created, **kwargs):
    if created:
        if instance.is_superuser or instance.is_staff:
            return
        group = Group.objects.get(
                pk=instance.edu_group.value)
        group.user_set.add(instance)


post_save.connect(send_activation_email, sender=User)
post_save.connect(add_user_to_group, sender=User)
post_save.connect(send_activation_email, sender=ProvinceUser)
post_save.connect(add_user_to_group, sender=ProvinceUser)
