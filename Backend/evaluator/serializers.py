from rest_framework import serializers
from .models import IdeaEvaluate, Idea

class IdeaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Idea
        fields = '__all__'  # Include all fields
class IdeaEvaluateSerializer(serializers.ModelSerializer):
    class Meta:
        model = IdeaEvaluate
        fields = '__all__'
