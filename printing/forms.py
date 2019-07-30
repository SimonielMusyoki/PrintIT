from .models import PrintItem
from django import forms

class PrintItemCreations(forms.ModelForm):
    

    class Meta:
        model = PrintItem
        fields = ('upload','pages','copies','printer','owner',)