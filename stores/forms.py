from django import forms
from .models import Store, StoreItem


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = "__all__"


class StoreItemForm(forms.ModelForm):
    class Meta:
        model = StoreItem
        fields = "__all__"
