from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import Profile

class CustomAuthenticationForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'label': 'form-control',})
        self.fields['username'].label = ""
        self.fields['password'].widget.attrs.update({'class': 'form-control',})
        self.fields['password'].label = ""

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['birth_year', 'postcode', 'gender']
        widgets = {
            'birth_year': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'yyyy'}),
            'postcode': forms.NumberInput(attrs={'class': 'form-control',}),
            'gender': forms.Select(attrs={'class': 'form-control',}),
        }

