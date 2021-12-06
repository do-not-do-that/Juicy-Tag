from django import forms
from .models import JuicyBoard
from django.forms.widgets import NumberInput
class JuicyForm(forms.ModelForm):
    class Meta:
        model = JuicyBoard
        fields = ('title', 'content','end_date')
    end_date = forms.DateTimeField(widget=NumberInput(attrs={'type': 'date'}), label="End_date")