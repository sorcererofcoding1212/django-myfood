from .models import Item
from django.forms import ModelForm


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ["item_name", "item_desc", "item_price", "item_photo"]
