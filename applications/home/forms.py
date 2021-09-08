from django import forms
from django.forms.forms import Form

class PruebaForm(forms.ModelForm):

    class Meta:
        model = []
        fields=(
            '',
            '',
            '',
        )
        widgets = {
            #se coloca el atributo
            '': forms.TextInput(
                attrs= {
                    'placeholder': 'aqui se pone esto'
                }
            )
        }
    
    #te permite recuperar el valor del campo para realizar validaciones
    def clean_FIELD(self):
        FIELD = self.cleaned_data['']

        if '' == '':
            raise forms.ValidationError('error aqui')
    
         
    
        return FIELD
