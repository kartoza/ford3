from django.db.models.signals import post_save
from django.contrib.auth.models import Group
from ford3.models.user import User, ProvinceUser
from ford3.notifier import Notifier
from ford3.models.qualification import Qualification
from ford3.models.campus import Campus
from ford3.completion_audit.completion_audit import CompletionAudit


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


def audit_for_publish(sender, instance, created, **kwargs):
    instance.audit_for_publish()


def completion_audit(sender, instance, created, **kwargs):
    completion_rate = CompletionAudit(
        instance, sender.COMPLETION_RULES).run()

    # prevent infinite loop
    sender.objects.filter(pk=instance.pk).update(
        completion_rate=completion_rate)


post_save.connect(send_activation_email, sender=User)
post_save.connect(add_user_to_group, sender=User)
post_save.connect(send_activation_email, sender=ProvinceUser)
post_save.connect(add_user_to_group, sender=ProvinceUser)
post_save.connect(audit_for_publish, sender=Qualification)
post_save.connect(completion_audit, sender=Campus)
post_save.connect(completion_audit, sender=Qualification)
