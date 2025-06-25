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

    path("trainers/", views.trainer_list, name="trainer_list"),
    path("trainers/add/", views.add_trainer, name="add_trainer"),
    path("trainers/<int:id>/edit/", views.edit_trainer, name="edit_trainer"),
    path("trainers/<int:id>/delete/", views.delete_trainer, name="delete_trainer"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)