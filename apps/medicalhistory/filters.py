import django_filters
from rest_framework.pagination import PageNumberPagination
from .models import MedicalHistory

class MedicalHistoryFilter(django_filters.FilterSet):

    class Meta:
        model = MedicalHistory
        fields = [ "created", "patient" ]


class MedicalHistoryPagination(PageNumberPagination):
    page_size_query_param = "page_size"
    # max_page_size = 100
    # page_size = 20

    
class ReportMedicalHistoryFilter(django_filters.FilterSet):
    range_created = django_filters.DateFromToRangeFilter(
        field_name="created", label="Range Created Date"
    )

    class Meta:
        model = MedicalHistory
        fields = [ "created", "patient", "range_created" ]