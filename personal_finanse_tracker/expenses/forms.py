from django import forms
from .models import Expense

class ExpenseForms(forms.ModelForm):
    class Meta:
        model=Expense
        fields=['title','amount','category']
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'amount':forms.NumberInput(attrs={'class':'form-control'}),
            'category':forms.Select(attrs={'class':'form-select'}),

        }