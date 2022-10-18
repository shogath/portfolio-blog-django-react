from smtplib import SMTPException
from django.core.mail import send_mail
from django.conf import settings
from celery import shared_task


@shared_task()
def send_contact_email_task(email_subject, email_message):
    """Sends an email when the contact form has been submitted."""
    try:
        send_mail(
            email_subject,
            email_message,
            settings.DJANGO_CONTACT_EMAIL,
            settings.DJANGO_ADMIN_EMAILS,
        )
    except SMTPException as e:  # It will catch other errors related to SMTP.
        print("There was an error sending an email." + e)
    except:  # It will catch All other possible errors.
        print("Mail Sending Failed!")
