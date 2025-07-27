from rest_framework import serializers
from drf_writable_nested.serializers import WritableNestedModelSerializer
from .models import *

class PhysicalExamSerializer(serializers.ModelSerializer):
    class Meta:
        model = PhysicalExam
        exclude = ['medicalHistory']

class DiagnosticSupportSerializer(serializers.ModelSerializer):
    class Meta:
        model = DiagnosticSupport
        exclude = ['medicalHistory']

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        exclude = ['medicalHistory']

class AttachmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attachment
        exclude = ['medicalHistory']

class TreatmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Treatment
        exclude = ['medicalHistory']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        exclude = ['medicalHistory']

class MedicalHistorySerializer(WritableNestedModelSerializer):
    physical_exam = PhysicalExamSerializer(required=False)
    diagnosis = DiagnosisSerializer(many=True, required=False)
    treatments = TreatmentSerializer(many=True, required=False)
    notes = NoteSerializer(required=False)

    class Meta:
        model = MedicalHistory
        fields = '__all__'
