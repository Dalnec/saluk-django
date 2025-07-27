import django_filters
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from .models import Patient

class PatientFilter(django_filters.FilterSet):
    patient_names = django_filters.CharFilter(method="filter_patient_names")

    class Meta:
        model = Patient
        fields = [ "code", "ci", "names", "lastnames", "birthdate", "gender", 
                  "phone", "email", "patient_names", ]

    def filter_patient_names(self, queryset, name, value):
        return queryset.filter(Q(names__icontains=value) | Q(lastnames__icontains=value))


class PatientPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    # max_page_size = 100
    page_size = 20