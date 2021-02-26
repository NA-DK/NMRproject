from django import forms
from .models import Formula,Name

class Formula_form(forms.ModelForm):
    class Meta:
        model = Formula
        fields = ['formula']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder':'분자식 입력',}),
        }
        labels = {
            'formula' : '분자식'
        }

class Name_form(forms.ModelForm):
    class Meta:
        model = Name
        fields = ['name']
        widgets = {
            'subject': forms.TextInput(attrs={'placeholder':'분자식 입력',}),
        }
        labels = {
            'name' : '분자명'
        }
