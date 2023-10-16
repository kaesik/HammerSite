import django_tables2 as tables
from .models import Item


class ItemTable(tables.Table):
    class Meta:
        model = Item
        fields = ['name', 'group', 'source']


class QualityFlawTable(tables.Table):
    class Meta:
        model = Item
        fields = ['name', 'group', 'source']