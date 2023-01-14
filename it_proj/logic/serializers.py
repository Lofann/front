from rest_framework import serializers
from .models import Descriptions

class DescriptionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Descriptions
        fields = ('name', 'content')