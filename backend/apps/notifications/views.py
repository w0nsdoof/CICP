from rest_framework import viewsets, permissions
from rest_framework.pagination import PageNumberPagination

from .models import Notification
from .serializers import NotificationSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'  
    max_page_size = 100  

class NotificationViewSet(viewsets.ModelViewSet):
    queryset = Notification.objects.all().order_by('-created_at')
    serializer_class = NotificationSerializer
    permission_classes = [permissions.IsAuthenticated]
    pagination_class = StandardResultsSetPagination

    def get_queryset(self):
        return self.queryset.filter(recipient=self.request.user)

    def perform_create(self, serializer):
        sender = self.request.user if self.request.user.is_authenticated else None
        serializer.save(sender=sender)
