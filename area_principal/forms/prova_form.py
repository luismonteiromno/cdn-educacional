from django import forms


class ProvaForm(forms.ModelForm):
    
    def clean(self):
        cleaned_data = super().clean()
        bimestre = cleaned_data.get('bimestre')
        
        if not bimestre:
            raise forms.ValidationError('O bimestre é obrigatório!')
        
        return cleaned_data
    