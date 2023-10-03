from itertools import chain, islice
from .models import *


def create_item(item):
    id = getattr(item, 'id')
    name = getattr(item, 'name')
    group = getattr(item, 'group')
    source = getattr(item, 'source')

    created_item = Item.objects.update_or_create(
        id=id,
        defaults={
            'name': name,
            'group': group,
            'source': source
        }
    )


db_weapons = ItemWeapon.objects.values_list('id', 'name', 'group', 'source')
db_armours = ItemArmour.objects.values_list('id', 'name', 'group', 'source')
db_ammunition = ItemAmmunition.objects.values_list('id', 'name', 'group', 'source')
db_items = ItemOther.objects.values_list('id', 'name', 'group', 'source')
db_items.union(db_weapons, db_armours, db_ammunition)
