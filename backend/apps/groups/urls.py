from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GroupSpaceViewSet

router = DefaultRouter()
router.register(r'groups', GroupSpaceViewSet, basename='news')

urlpatterns = router.urls