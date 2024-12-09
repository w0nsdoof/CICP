from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from apps.news.urls import router as news_router
from apps.groups.urls import router as groups_router
from apps.notifications.urls import router as notifications_router

router = DefaultRouter()
router.registry.extend(news_router.registry)
router.registry.extend(groups_router.registry)
router.registry.extend(notifications_router.registry)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('apps.authentication.urls')),  
    path('api/', include(router.urls)),   
]
