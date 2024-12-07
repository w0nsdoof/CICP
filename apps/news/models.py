from django.db import models
from django.utils.translation import gettext_lazy as _

from apps.authentication.models import User

class News(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='news_posts')

    # Optional fields for more context
    summary = models.TextField(blank=True, null=True)
    tags = models.ManyToManyField('Tag', blank=True)
    
    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name_plural = 'News'
        ordering = ['-created_at']

    def __str__(self):
        return self.title

class Tag(models.Model):
    """
    Tags for categorizing news articles
    """
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
