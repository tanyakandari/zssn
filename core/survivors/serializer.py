from rest_framework.serializers import ModelSerializer
from .models import Survivor

class SurvivorSerializer(ModelSerializer):
    class Meta:
        fields = '__all__'
        model = Survivor
