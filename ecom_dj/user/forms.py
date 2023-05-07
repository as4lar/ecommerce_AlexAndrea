from .models import User
from django import forms
class UserCreate(forms.ModelForm):
    class Meta:
        model=User
        fields='__all__'