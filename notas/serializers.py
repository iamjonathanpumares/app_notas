from .models import Nota
from rest_framework import serializers

class NotaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nota
        fields = ['id', 'title', 'content']