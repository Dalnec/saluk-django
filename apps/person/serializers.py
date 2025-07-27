from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()
    gender_description = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = "__all__"