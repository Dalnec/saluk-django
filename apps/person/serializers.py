import json
from rest_framework import serializers
from .models import *

class PatientSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()
    gender_description = serializers.ReadOnlyField()

    class Meta:
        model = Patient
        fields = "__all__"


class ReportPatientSerializer(serializers.ModelSerializer):
    full_name = serializers.ReadOnlyField()
    age = serializers.ReadOnlyField()
    gender_description = serializers.ReadOnlyField()
    count_records = serializers.SerializerMethodField()
    allergies_description = serializers.SerializerMethodField()

    class Meta:
        model = Patient
        fields = [
            "code",
            "ci",
            "full_name",
            "gender_description",
            "birthdate",
            "age",
            "phone",
            "address",
            "allergies_description",
            "count_records",
        ]
    
    def get_count_records(self, obj) -> int:
        return obj.medical_histories.count()

    def get_allergies_description(self, obj) -> str:
        return ", ".join(map(str, json.loads(obj.allergies)))