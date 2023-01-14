from rest_framework import viewsets, permissions
from .serializers import HomeSerializer, DemandSerializer, GeographySerializer,SkillsSerializer
from .models import Home, Demand, Skills, Geography
from rest_framework.response import Response


class HomeViewSet(viewsets.ModelViewSet):
    serializer_class = HomeSerializer
    queryset = Home.objects.all()

    permission_classes = [permissions.AllowAny]

class DemandViewSet(viewsets.ModelViewSet):
    serializer_class = DemandSerializer
    queryset = Demand.objects.all()

    permission_classes = [permissions.AllowAny]

class GeographyViewSet(viewsets.ModelViewSet):
    serializer_class = GeographySerializer
    queryset = Geography.objects.all()

    permission_classes = [permissions.AllowAny]

class SkillsViewSet(viewsets.ModelViewSet):
    serializer_class = SkillsSerializer
    queryset = Skills.objects.all()

    permission_classes = [permissions.AllowAny]