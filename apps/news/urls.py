from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewSet, TagViewSet

router = DefaultRouter()
router.register(r'news', NewsViewSet, basename='news')
router.register(r'tags', TagViewSet, basename='tag')

urlpatterns = [
    path('', include(router.urls)),
]