from django.db import models

# Create your models here.
class Pokemon(models.Model):
    name = models.CharField(max_length=100, null=False)
    description = models.TextField(null=True, blank=True)
    height = models.FloatField()
    weight = models.FloatField()
    base_experience = models.IntegerField()
    types = models.CharField(max_length=100)
    abilities = models.CharField(max_length=100)
    stats = models.CharField(max_length=100)
    image = models.ImageField(upload_to='pokemon_images/', null=True, blank=True)

    def __str__(self):
        return self.name
    