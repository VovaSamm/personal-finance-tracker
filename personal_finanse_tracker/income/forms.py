from django import forms
from .models import Income

class IncomeForm(forms.ModelForm):
    class Meta:
        model=Income
        fields = ['title', 'amount', 'source']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'source': forms.Select(attrs={'class': 'form-select'}),

        }