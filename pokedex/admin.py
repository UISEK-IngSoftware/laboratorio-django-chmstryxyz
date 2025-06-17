from django.contrib import admin
from .models import Pokemon, Trainer
from django.utils.html import format_html

@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    list_display = ('name', 'types', 'weight', 'height', 'trainer', 'image_tag')

    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.image.url))
        return "No Image"
    image_tag.short_description = 'Image'

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'user')