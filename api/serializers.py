from rest_framework import serializers
from pokedex.models import Pokemon, Trainer
import base64
from django.core.files.base import ContentFile
import uuid


class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str) and data.startswith('data:image'):
            format, imgstr = data.split(';base64,')
            ext = format.split('/')[-1]
            id = uuid.uuid4()
            file_name = f"{str(id)}.{ext}"
            data = ContentFile(base64.b64decode(imgstr), name=file_name)
        return super().to_internal_value(data)


class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = ['id', 'nombre', 'apellido', 'nivel']


class PokemonSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(
        max_length=None, use_url=True, source='image', required=False, allow_null=True
    )

    type = serializers.CharField(source='types')

    trainer = TrainerSerializer(read_only=True)
    trainer_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Pokemon
        fields = [
            'id', 'name', 'type', 'weight', 'height', 'picture', 'description', 'abilities', 'trainer', 'trainer_id'
        ]

        read_only_fields = ['trainer']

    def create(self, validated_data):
        trainer_id = validated_data.pop('trainer_id', None)
        description = validated_data.pop('description', None)
        abilities = validated_data.pop('abilities', []) 

        pokemon = Pokemon.objects.create(**validated_data)
        if trainer_id:
            try:
                trainer = Trainer.objects.get(pk=trainer_id)
                pokemon.trainer = trainer
                pokemon.save()
            except Trainer.DoesNotExist:
                pass
        
        if description is not None:
            pokemon.description = description
        pokemon.abilities = abilities 
        pokemon.save()

        return pokemon

    def update(self, instance, validated_data):
        trainer_id = validated_data.pop('trainer_id', None)
        description = validated_data.pop('description', None)
        abilities = validated_data.pop('abilities', None)

        if trainer_id is not None:
            try:
                instance.trainer = Trainer.objects.get(pk=trainer_id)
            except Trainer.DoesNotExist:
                instance.trainer = None 
        
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        
        if description is not None:
            instance.description = description
        if abilities is not None:
            instance.abilities = abilities
            
        instance.save()
        return instance