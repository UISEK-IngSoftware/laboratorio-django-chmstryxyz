from django.db import models
from django.contrib.auth.models import User 

class Trainer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

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
    types = models.CharField(max_length=100, choices=TIPE_CHOICES)
    weight = models.FloatField(help_text="en kg")
    height = models.FloatField(help_text="en m")
    trainer = models.ForeignKey(Trainer, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='pokemon_images/', null=True, blank=True, verbose_name="Fotografía")


    def __str__(self):
        return self.name