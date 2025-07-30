from rest_framework import status
from drf_spectacular.utils import extend_schema
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
# from django.db.models import Sum
from .filters import *
from .models import *
from .serializers import *


@extend_schema( tags=["ReportMedicalHistory"], )
class ReportMedicalHistoryView(XLSXFileMixin, ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = ReportMedicalHistoryFilter
    queryset = MedicalHistory.objects.all().order_by("-created")
    
    serializer_class = ReportMedicalHistorySerializer
    renderer_classes = (XLSXRenderer,)
    filename = "reporte_historial.xlsx"

    column_header = {
        "titles": [
            "FECHA",
            "DNI",
            "NOMBRE",
            "GENERO",
            "EDAD",
            "ALERGIAS",
            "ANAMNESIS",
            "EXAMEN FISICO",
            "DIAGNOSTICO",
            "TRATAMIENTO",
            "NOTAS",
            "OBSERVACIONES",
        ],
        "column_width": [18, 14, 35, 10, 10, 18, 60, 60, 40, 40, 16, 16],
        "height": 15,
        "style": {
            "fill": {
                "fill_type": "solid",
                "start_color": "FE879C",
            },
            "alignment": {
                "horizontal": "center",
                "vertical": "center",
                "wrapText": True,
                "shrink_to_fit": True,
            },
            "border_side": {
                "border_style": "thin",
                "color": "FF000000",
            },
            "font": {
                "name": "Arial",
                "size": 10,
                "bold": True,
                "color": "FF000000",
            },
        },
    }
    body = {
        "height": 45,
        "style": {
            "alignment": {
                "horizontal": "center",
                "vertical": "center",
                "wrapText": True,
                "shrink_to_fit": True,
            },
            "border_side": {
                "border_style": "thin",
                "color": "FF000000",
            },
            "font": {
                "name": "Arial",
                "size": 10,
                "bold": False,
                "color": "FF000000",
            },
        },
    }

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        queryset = self.filter_queryset(queryset)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)