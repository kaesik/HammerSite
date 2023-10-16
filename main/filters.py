import django_filters
from django_filters import CharFilter
from .models import *


class ItemFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    group = CharFilter(field_name='group', lookup_expr='icontains')
    source = CharFilter(field_name='source', lookup_expr='icontains')

    class Meta:
        model = Item
        fields = ['name', 'group', 'source']


class QualityFlawFilter(django_filters.FilterSet):
    name = CharFilter(field_name='name', lookup_expr='icontains')
    group = CharFilter(field_name='group', lookup_expr='icontains')
    source = CharFilter(field_name='source', lookup_expr='icontains')

    class Meta:
        model = QualityFlaw
        fields = ['name', 'group', 'source']
