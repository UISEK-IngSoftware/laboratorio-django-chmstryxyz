from django import forms
from .models import Pokemon, Trainer

class PokemonForm(forms.ModelForm):
 
    trainer = forms.ModelChoiceField(queryset=Trainer.objects.all(), required=False, label="Entrenador")

    class Meta:
        model = Pokemon
        fields = [
            'name', 'types', 'weight', 'height', 'trainer', 'image'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'types': forms.Select(attrs={'class': 'form-control'}),
            'weight': forms.NumberInput(attrs={'class': 'form-control'}),
            'height': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Nombre',
            'types': 'Tipo',
            'weight': 'Peso',
            'height': 'Altura',
            'image': 'Fotografía',
        }

class TrainerForm(forms.ModelForm):
    class Meta:
        model = Trainer
        fields = ['nombre', 'apellido', 'nivel']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'nivel': forms.NumberInput(attrs={'class': 'form-control'}),
        }