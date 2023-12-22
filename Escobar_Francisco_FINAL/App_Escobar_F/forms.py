from django import forms
from .models import Institucion,Inscrito

class InscritoForm(forms.ModelForm):
    class Meta:
        model = Inscrito
        fields = "__all__"
    
class InstitucionForm(forms.ModelForm):
    class Meta:
        model = Institucion
        fields = "__all__"
    