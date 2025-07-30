import requests
from urllib3.exceptions import InsecureRequestWarning
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet
from rest_framework.decorators import action
from drf_spectacular.utils import extend_schema
from drf_excel.mixins import XLSXFileMixin
from drf_excel.renderers import XLSXRenderer
from .models import Patient
from .serializers import *
from .filters import PatientFilter, PatientPagination

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

@extend_schema(tags=["Patient"])
class PatientView(viewsets.GenericViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all().order_by("-id")
    filter_backends = [DjangoFilterBackend]
    filterset_class = PatientFilter
    pagination_class = PatientPagination

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        document = request.data.get("ci", None)
        if document is None:
            return  Response({"success": False, "message":"El campo 'ci' es requerido"})
        patient = Patient.objects.filter(ci=document)
        if patient.exists() and document != "-":
            return  Response({"success": False, "message":f"El numero de documento '{document}' ya se encuentra registrado"})
        serializer.is_valid(raise_exception=True)
        patient = serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    @action(detail=False, methods=["get"], url_path="apiclient/(?P<document>[0-9]+)")
    def apiclient(self, request, document=None):
        import environ
        env = environ.Env()
        token = env("API_TOKEN")
        url = env("API_URL")
        header = {
            'Content-Type': 'application/json',
            'Authorization': 'Bearer {}'.format(token)
        }
        
        if len(document) != 8:
            return  Response({"success": False, "message":f"No es un número válido {document}"})
        patient = Patient.objects.filter(ci=document)
        if patient.exists():
            return  Response({"success": False, "message":f"El numero de documento '{document}' ya se encuentra registrado"})
        url = f'{url}/dni/' + document

        response = requests.get(url, headers=header, verify=False)
        if response.status_code == 200:
            return  Response(response.json(), status=status.HTTP_200_OK)
        elif response.status_code == 404:
            return  Response({"success": False, "message":"No encontrado!"})
        else:
            return  Response({"success": False, "message":"Error!"})


@extend_schema( tags=["ReportPatient"], )
class ReportPatientView(XLSXFileMixin, ReadOnlyModelViewSet):
    filter_backends = [DjangoFilterBackend]
    filterset_class = PatientFilter
    queryset = Patient.objects.all().order_by("-created")
    
    serializer_class = ReportPatientSerializer
    renderer_classes = (XLSXRenderer,)
    filename = "reporte_pacientes.xlsx"

    column_header = {
        "titles": [
            "CODIGO",
            "DNI",
            "NOMBRE COMPLETO",
            "GENERO",
            "F. NACIMIENTO",
            "EDAD",
            "TELEFONO",
            "DIRECCION",
            "ALERGIAS",
            "# CONSULTAS",
        ],
        "column_width": [12, 12, 45, 10, 18, 10, 12, 35, 35, 14],
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
        "height": 15,
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