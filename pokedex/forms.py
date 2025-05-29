from django import forms
from .models import Pokemon

TIPE_CHOICES = [
    ('normal', 'Normal'),
    ('fighting', 'Lucha'),
    ('flying', 'Volador'),
    ('poison', 'Veneno'),
    ('ground', 'Tierra'),
    ('rock', 'Roca'),
    ('bug', 'Bicho'),
    ('ghost', 'Fantasma'),
    ('steel', 'Acero'),
    ('fire', 'Fuego'),
    ('water', 'Agua'),
    ('grass', 'Planta'),
    ('electric', 'Eléctrico'),
    ('psychic', 'Psíquico'),
    ('ice', 'Hielo'),
    ('dragon', 'Dragón'),
    ('dark', 'Siniestro'),
    ('fairy', 'Hada'),
]

class PokemonForm(forms.ModelForm):
    types = forms.ChoiceField(
        choices=TIPE_CHOICES,
        widget=forms.Select()
    )

    class Meta:
        model = Pokemon
        fields = [
            'name', 'description', 'height', 'weight',
            'base_experience', 'types', 'abilities', 'stats', 'image'
        ]
        widgets = {
            'description': forms.Textarea(attrs={
                'rows': 4,
                'style': 'resize: none;'
            }),
            'image': forms.ClearableFileInput(),
        }
        labels = {
            'name': 'Nombre',
            'description': 'Descripción',
            'height': 'Altura (m)',
            'weight': 'Peso (kg)',
            'base_experience': 'Experiencia base',
            'types': 'Tipos',
            'abilities': 'Habilidades',
            'stats': 'Estadísticas',
            'image': 'Imagen',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs.update({
                'class': 'form-control',
            })