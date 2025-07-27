from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r"medicalhistory", MedicalHistoryView, basename="medicalhistory")
router.register(r"physicalexam", PhysicalExamView, basename="physicalexam")
router.register(r"diagnosticsupport", DiagnosticSupportView, basename="diagnosticsupport")
router.register(r"diagnosis", DiagnosisView, basename="diagnosis")
router.register(r"treatment", TreatmentView, basename="treatment")
router.register(r"attachment", AttachmentView, basename="attachment")
router.register(r"note", NoteView, basename="note")

urlpatterns = [
    path("", include(router.urls)),
]
