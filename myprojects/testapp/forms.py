from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'age', 'position']
        labels = {
            'name': '',
            'age': '',
            'position': '',
        }
        widgets = {
            'name': forms.TextInput(attrs={'class': 'input','type':'text','placeholder': 'Name','required': 'required'}),
            'age': forms.NumberInput(attrs={'class': 'input','type':'text', 'placeholder': 'Age','required': 'required'}),
            'position': forms.TextInput(attrs={'class': 'input', 'type':'text','placeholder': 'Position','required': 'required'}),
        }