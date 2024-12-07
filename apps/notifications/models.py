from django.db import models

from apps.authentication.models import User

class Notification(models.Model):
    TYPE_CHOICES = (
        ('info', 'Information'),
        ('alert', 'Alert'),
        ('message', 'Message'),
    )
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_notifications')
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receive_notifications')
    content = models.TextField()
    type = models.CharField(max_length=20, choices=TYPE_CHOICES, default='info')
    is_read = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.recipient.username} - {self.type}"
    
    class Meta:
        indexes = [
            models.Index(fields=['created_at'])
        ]
