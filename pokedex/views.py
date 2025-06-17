from django.shortcuts import get_object_or_404, redirect, render
from .models import Pokemon
from .forms import PokemonForm
from django.contrib.auth.decorators import login_required # Para proteger vistas

def index(request):
    pokemons = Pokemon.objects.order_by('name')
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon_detail(request, id: int):
    # Usamos get_object_or_404 para manejar casos donde el Pokémon no existe
    pokemon = get_object_or_404(Pokemon, pk=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

@login_required # Decorador para que solo usuarios logueados accedan
def add_pokemon(request):
    if request.method == 'POST':
        # Pasamos request.POST para datos del form y request.FILES para los archivos
        form = PokemonForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = PokemonForm()
    
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def edit_pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, pk=id)
    if request.method == 'POST':
        form = PokemonForm(request.POST, request.FILES, instance=pokemon)
        if form.is_valid():
            form.save()
            return redirect("pokedex:index")
    else:
        form = PokemonForm(instance=pokemon)
    
    return render(request, 'pokemon_form.html', {'form': form})

@login_required
def delete_pokemon(request, id: int):
    pokemon = get_object_or_404(Pokemon, pk=id)
    if request.method == 'POST': # Para confirmar la eliminación
        pokemon.delete()
        return redirect('pokedex:index')
    # Idealmente, aquí se mostraría una página de confirmación.
    # Por simplicidad, lo haremos directo en la vista de lista.
    # Para hacerlo correctamente, crea un template `confirm_delete.html`.
    # Aquí un ejemplo de cómo se vería la confirmación en el template de lista:
    # Se podría usar un modal de Bootstrap para confirmar antes de redirigir a esta URL.
    # Por ahora, para simplificar, eliminamos directamente.
    pokemon.delete()
    return redirect('pokedex:index')