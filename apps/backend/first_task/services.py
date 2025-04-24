from django.conf import settings
from django.core.mail import send_mail
from first_task.models import Mails


def send_emails(subject, message, recipient_list):
    """Сервис для отправки письма и сохранения в бд"""
    for recipient in recipient_list:
        mail = Mails.objects.create(
            subject=subject, message=message, recipient=recipient
        )
    try:
        send_mail(subject, message, settings.EMAIL_HOST_USER, recipient_list)
        mail.is_sent = True
        status = "Письма были успешно отправлены"
    except:
        mail.is_sent = False
        status = "Письма не были успешно отправлены"
    mail.save()
    return message
