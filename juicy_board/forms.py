from django import forms
from .models import JuicyBoard

class JuicyForm(forms.ModelForm):
    class Meta:
        model = JuicyBoard
        fields = {'title', 'content'}