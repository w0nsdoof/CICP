from rest_framework import viewsets, permissions, status
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from .models import GroupSpace
from .serializers import GroupSpaceSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'  
    max_page_size = 100  

class GroupSpaceViewSet(viewsets.ModelViewSet):
    queryset = GroupSpace.objects.all()
    serializer_class = GroupSpaceSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        existing_GroupSpace = GroupSpace.objects.filter(name=serializer.validated_data['name']).first()
        if existing_GroupSpace:
            return Response({
                'message': 'GroupSpace already exists', 
                'group': GroupSpaceSerializer(existing_GroupSpace).data
            }, status=status.HTTP_200_OK)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)