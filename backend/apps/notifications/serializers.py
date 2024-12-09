from rest_framework import serializers

from .models import Notification

class NotificationSerializer(serializers.ModelSerializer):
    sender = serializers.StringRelatedField(read_only=True)  # Displays sender's username
    
    class Meta:
        model = Notification
        fields = ['id', 'sender', 'recipient', 'content', 'type', 'is_read', 'created_at']