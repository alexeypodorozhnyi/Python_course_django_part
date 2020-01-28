from django.forms import ModelForm, HiddenInput

from .models import ShoppingEvent, Item, ReversalEvent


class ShoppingEventForm(ModelForm):
    class Meta:
        model = ShoppingEvent
        fields = ('count_of_items', 'item','order_sum')
        widgets = {'item': HiddenInput(),'order_sum': HiddenInput()}


class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ('name', 'detail_info', 'price', 'image', 'count_items')


class ReversalForm(ModelForm):
    class Meta:
        model = ReversalEvent
        fields = ('is_confirmed',)
        widgets = {'is_confirmed': HiddenInput()}
