from rest_framework import serializers
from .models import Home, Demand, Skills, Geography

class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = ('title', 'text', 'image')

class DemandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Demand
        fields = ('title', 'text', 'graph_first', 'graph_second',)

class GeographySerializer(serializers.ModelSerializer):
    class Meta:
        model = Geography
        fields = ('title', 'text', 'table', 'graph')

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ('title', 'text', 'graph')


