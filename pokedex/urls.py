from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = "pokedex"
urlpatterns = [
    path("", views.index, name="index"),
    path("pokemon/<int:id>/", views.pokemon_detail, name="pokemon_detail"),
    path("pokemon/add/", views.add_pokemon, name="add_pokemon"),
    path("pokemon/<int:id>/edit/", views.edit_pokemon, name="edit_pokemon"),
    path("pokemon/<int:id>/delete/", views.delete_pokemon, name="delete_pokemon"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)