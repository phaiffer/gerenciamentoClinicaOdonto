from django import forms

from ..models import EnderecoPaciente

class EnderecoPacienteForm(forms.ModelForm):
    class Meta:
        model = EnderecoPaciente
        fields = ['rua', 'cidade', 'estado']