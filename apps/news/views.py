from rest_framework import viewsets, permissions
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from django.views.decorators.cache import cache_page

from .models import News, Tag
from .serializers import NewsSerializer, TagSerializer

class StandardResultsSetPagination(PageNumberPagination):
    page_size = 10 
    page_size_query_param = 'page_size'  
    max_page_size = 100  

@cache_page(60 * 10) # 10 min
class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    pagination_class = StandardResultsSetPagination

    def perform_create(self, serializer):
        # Automatically set the author to the current user
        serializer.save(author=self.request.user)

    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=partial)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)
    
    def perform_update(self, serializer):
        serializer.save()

    def get_queryset(self):
        queryset = News.objects.all()
        
        # Filter by author
        author = self.request.query_params.get('author', None)
        if author:
            try:
                author_id = int(author)
                queryset = queryset.filter(author__id=author_id)
            except ValueError:
                queryset = queryset.filter(author__username=author)
        
        search_query = self.request.query_params.get('search', None)
        if search_query:
            queryset = queryset.filter(
                title__icontains=search_query
            ) | queryset.filter(
                content__icontains=search_query
            )
        
        return queryset.order_by('-created_at')

@cache_page(60 * 10)
class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [permissions.IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        existing_tag = Tag.objects.filter(name=serializer.validated_data['name']).first()
        if existing_tag:
            return Response({
                'message': 'Tag already exists', 
                'tag': TagSerializer(existing_tag).data
            }, status=status.HTTP_200_OK)
        
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)