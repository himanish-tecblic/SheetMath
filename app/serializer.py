from rest_framework import serializers
from app.models import *
class PBPMSerializer(serializers.ModelSerializer):
    class Meta:
        model = PBPM
        fields = "__all__"

