from rest_framework import serializers

from .models import GroupSpace

class GroupSpaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroupSpace
        fields = ['id', 'name', 'description', 'reference']
