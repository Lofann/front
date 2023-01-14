from django.shortcuts import render

# Create your views here.
from .models import Descriptions
from .serializers import DescriptionsSerializer
from rest_framework import generics

class DescriptionsListCrate(generics.ListCreateAPIView):
    queryset = Descriptions.objects.all()
    serializer_class = DescriptionsSerializer