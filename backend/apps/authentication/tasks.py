from celery import shared_task
from celery.utils.log import get_task_logger

from django.core.mail import send_mail
from django.conf import settings

logger = get_task_logger(__name__)

@shared_task(bind=True, max_retries=3)
def send_email_task(self, recipient, subject, body):
    try:
        send_mail(
            subject=subject,
            message=body,
            from_email=settings.EMAIL_HOST_USER,  
            recipient_list=[recipient],
            fail_silently=False,
        )
        logger.info(f"Email successfully sent to {recipient}")
    except Exception as exc:
        logger.error(f"Error sending email to {recipient}: {exc}")
        raise self.retry(exc=exc)