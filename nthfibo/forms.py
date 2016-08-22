from django import forms

from .models import Nthfibonacci

class NthfiboForm(forms.ModelForm):
    
    class Meta:
        model = Nthfibonacci
        fields = ('n', )





















