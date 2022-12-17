from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.template.loader import render_to_string
from django.utils.html import strip_tags

UserModel = get_user_model()


@receiver(signal=post_save, sender=UserModel)
def send_email_on_successful_sign_up(instance, created, **kwargs):
    if not created:
        return

    email_content = render_to_string('email_templates/successful_sign_up.html', {
        'user': instance,
    })

    send_mail(
        subject='Welcome to Weather&Pals!',
        message=strip_tags(email_content),
        html_message=email_content,
        from_email=settings.DEFAULT_FROM_EMAIL,
        recipient_list=(instance.email,),
    )


@receiver(models.signals.post_delete, sender=UserModel)
def handle_deleted_profile(sender, instance, **kwargs):
    if instance.shipper:
        instance.shipper.delete()
    if instance.carrier:
        instance.carrier.delete()
    if instance.affiliat:
        instance.affiliat.delete()