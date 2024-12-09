from django.db import models

class GroupSpace(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    reference = models.URLField()
    
    def __str__(self):
        return f"{self.name}"