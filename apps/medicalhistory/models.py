from django.db import models
from model_utils.models import TimeStampedModel

class MedicalHistory(TimeStampedModel):
    patient = models.ForeignKey("person.Patient", on_delete=models.CASCADE, related_name='medical_histories')
    # doctor = models.ForeignKey("auth.User", on_delete=models.SET_NULL, null=True, blank=True)
    # title = models.CharField(max_length=255)
    # summary = models.TextField(blank=True)

    def __str__(self):
        return f"Medical History #{self.pk} for {self.patient}"

class PhysicalExam(TimeStampedModel):
    medicalHistory = models.OneToOneField(MedicalHistory, on_delete=models.CASCADE, related_name='physical_exam')
    weight = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    height = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    summaryAnamnesis = models.TextField(null=True, blank=True)
    summaryPhysicalExam = models.TextField(null=True, blank=True)
    temperature = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)
    bloodPressureSystolic = models.IntegerField(null=True, blank=True)
    bloodPressureDiastolic = models.IntegerField(null=True, blank=True)
    heartRate = models.IntegerField(null=True, blank=True)
    respiratoryRate = models.IntegerField(null=True, blank=True)
    oxygenSaturation = models.DecimalField(max_digits=4, decimal_places=1, null=True, blank=True)

    def __str__(self):
        return f"Physical Exam of {self.medicalHistory.patient} on {self.created.date()}"


class DiagnosticSupport(TimeStampedModel):
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='diagnostic_supports')
    studyType = models.CharField(max_length=255)
    result = models.TextField()
    file = models.FileField(upload_to='diagnostic_supports/', null=True, blank=True)

    def __str__(self):
        return f"{self.studyType} for {self.medicalHistory.patient}"


class Diagnosis(TimeStampedModel):
    medicalHistory = models.OneToOneField(MedicalHistory, on_delete=models.CASCADE, related_name='diagnosis')
    # medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='diagnosis')
    # ciex = models.CharField(max_length=50, null=True, blank=True)
    description = models.TextField()
    # kind = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Diagnosis for {self.medicalHistory.patient}"

class Treatment(TimeStampedModel):
    medicalHistory = models.OneToOneField(MedicalHistory, on_delete=models.CASCADE, related_name='treatments')
    # medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='treatments')
    description = models.TextField()
    # concentration = models.CharField(max_length=100, null=True, blank=True)
    # presentation = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return f"Treatment for {self.medicalHistory.patient}"


class Attachment(TimeStampedModel):
    medicalHistory = models.ForeignKey(MedicalHistory, on_delete=models.CASCADE, related_name='attachments')
    description = models.CharField(max_length=255)
    file = models.FileField(upload_to='attachments/')

    def __str__(self):
        return f"Attachment for {self.medicalHistory.patient}"


class Note(TimeStampedModel):
    medicalHistory = models.OneToOneField(MedicalHistory, on_delete=models.CASCADE, related_name='notes')
    notes = models.TextField()
    observations = models.TextField()

    def __str__(self):
        return f"Note for {self.medicalHistory.patient}"


# class AuditLog(TimeStampedModel):
#     user = models.ForeignKey('auth.User', on_delete=models.CASCADE)
#     action = models.CharField(max_length=255)
#     model_name = models.CharField(max_length=100)
#     object_id = models.CharField(max_length=100)
#     snapshot = models.JSONField(null=True, blank=True)

#     def __str__(self):
#         return f"{self.user} {self.action} {self.model_name} ({self.object_id}) at {self.created}"