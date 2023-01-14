from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import HomeViewSet,SkillsViewSet,GeographyViewSet, DemandViewSet

router = DefaultRouter()
router.register('home', HomeViewSet, basename='home')
router.register('demand', DemandViewSet, basename='demand')
router.register('geography', GeographyViewSet, basename='geography')
router.register('skills', SkillsViewSet, basename='skills')



urlpatterns = [
    path("", include(router.urls))
]