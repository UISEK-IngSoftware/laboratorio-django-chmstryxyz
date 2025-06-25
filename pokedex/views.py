from django.shortcuts import get_object_or_404, redirect, render
from .models import Pokemon, Trainer
from .forms import PokemonForm, TrainerForm
from django.contrib.auth.decorators import login_required # Para proteger vistas

def index(request):
    pokemons = Pokemon.objects.order_by('name')
    return render(request, 'index.html', {'pokemons': pokemons})

def pokemon_detail(request, id: int):
    pokemon = get_object_or_404(Pokemon, pk=id)
    return render(request, 'pokemon_detail.html', {'pokemon': pokemon})

@login_required 
def add_pokemon(request):
    if request.method == 'POST':
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
    if request.method == 'POST': 
        pokemon.delete()
        return redirect('pokedex:index')

    pokemon.delete()
    return redirect('pokedex:index')

@login_required
def trainer_list(request):
    trainers = Trainer.objects.all()
    return render(request, 'trainer_list.html', {'trainers': trainers})

@login_required
def add_trainer(request):
    if request.method == 'POST':
        form = TrainerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainer_list')
    else:
        form = TrainerForm()
    return render(request, 'trainer_form.html', {'form': form, 'action': 'Añadir'})

@login_required
def edit_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    if request.method == 'POST':
        form = TrainerForm(request.POST, instance=trainer)
        if form.is_valid():
            form.save()
            return redirect('pokedex:trainer_list')
    else:
        form = TrainerForm(instance=trainer)
    return render(request, 'trainer_form.html', {'form': form, 'action': 'Editar'})

@login_required
def delete_trainer(request, id):
    trainer = get_object_or_404(Trainer, pk=id)
    trainer.delete()
    return redirect('pokedex:trainer_list')