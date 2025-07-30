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
    diagnosis = DiagnosisSerializer(required=False)
    treatments = TreatmentSerializer(required=False)
    notes = NoteSerializer(required=False)

    class Meta:
        model = MedicalHistory
        fields = '__all__'


class ReportMedicalHistorySerializer(serializers.ModelSerializer):
    patient_ci = serializers.ReadOnlyField(source="patient.ci")
    patient_fullname = serializers.ReadOnlyField(source="patient.full_name")
    # patient_names = serializers.ReadOnlyField(source="patient.names")
    # patient_lastnames = serializers.ReadOnlyField(source="patient.lastnames")
    patient_gender = serializers.ReadOnlyField(source="patient.gender")
    patient_age = serializers.ReadOnlyField(source="patient.age")
    patient_allergies = serializers.ReadOnlyField(source="patient.allergies")
    pe_summaryAnamnesis = serializers.ReadOnlyField(source="physical_exam.summaryAnamnesis")
    pe_summaryPhysicalExam = serializers.ReadOnlyField(source="physical_exam.summaryPhysicalExam")
    diagnostico_description = serializers.ReadOnlyField(source="diagnosis.description")
    treatment_description = serializers.ReadOnlyField(source="treatments.description")
    notes_notes = serializers.ReadOnlyField(source="notes.notes")
    notes_observations = serializers.ReadOnlyField(source="notes.observations")
    
    class Meta:
        model = MedicalHistory
        fields = [
            "created", 
            "patient_ci",
            "patient_fullname",
            # "patient_names",
            # "patient_lastnames",
            "patient_gender",
            "patient_age",
            "patient_allergies",
            "pe_summaryAnamnesis",
            "pe_summaryPhysicalExam",
            "diagnostico_description",
            "treatment_description",
            "notes_notes",
            "notes_observations",
        ]