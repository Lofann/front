from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet

router = DefaultRouter()
router.register('home', HomeViewSet, basename='home')
router.register('demand', HomeViewSet, basename='demand')
router.register('geography', HomeViewSet, basename='geography')
router.register('skills', HomeViewSet, basename='skills')


urlpatterns = [
    path("", include(router.urls))
]