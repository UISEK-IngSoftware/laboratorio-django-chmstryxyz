from django.contrib import admin
from .models import Pokemon
from django.utils.html import format_html
# Register your models here.
@admin.register(Pokemon)
class PokemonAdmin(admin.ModelAdmin):
    pass
    list_display = ('name', 'height', 'weight', 'base_experience', 'types', 'abilities', 'stats', 'image_tag')
    def image_tag(self, obj):
        if obj.image:
            return format_html('<img src="{}" style="width: 100px; height: auto;" />'.format(obj.image.url))
        return "No Image"
    image_tag.short_description = 'Image'