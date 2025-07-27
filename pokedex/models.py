from django.db import models

class Trainer(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    nivel = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Pokemon(models.Model):
    name = models.CharField(max_length=100)
    TIPE_CHOICES = [
        ('normal', 'Normal'), ('fighting', 'Lucha'), ('flying', 'Volador'),
        ('poison', 'Veneno'), ('ground', 'Tierra'), ('rock', 'Roca'),
        ('bug', 'Bicho'), ('ghost', 'Fantasma'), ('steel', 'Acero'),
        ('fire', 'Fuego'), ('water', 'Agua'), ('grass', 'Planta'),
        ('electric', 'Eléctrico'), ('psychic', 'Psíquico'), ('ice', 'Hielo'),
        ('dragon', 'Dragón'), ('dark', 'Siniestro'), ('fairy', 'Hada'),
    ]
    
    types = models.CharField(max_length=100, choices=TIPE_CHOICES, verbose_name="Tipo")
    weight = models.FloatField(help_text="en kg", verbose_name="Peso")
    height = models.FloatField(help_text="en m", verbose_name="Altura")
    
    trainer = models.ForeignKey(Trainer, on_delete=models.SET_NULL, null=True, blank=True)
    image = models.ImageField(upload_to='pokemon_images/', null=True, blank=True, verbose_name="Fotografía")

    description = models.TextField(blank=True, null=True, verbose_name="Descripción")
    abilities = models.JSONField(blank=True, null=True, default=list, verbose_name="Habilidades")
    
    def __str__(self):
        return self.name