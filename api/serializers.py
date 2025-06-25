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
        max_length=None, use_url=True, source='image', required=False
    )

    type = serializers.CharField(source='types')
    

    trainer = TrainerSerializer(read_only=True)

    trainer_id = serializers.IntegerField(write_only=True, required=False, allow_null=True)

    class Meta:
        model = Pokemon

        fields = [
            'id', 'name', 'type', 'weight', 'height', 'picture', 'trainer', 'trainer_id'
        ]

        read_only_fields = ['trainer']

    def create(self, validated_data):

        trainer_id = validated_data.pop('trainer_id', None)

        if trainer_id:
            trainer = Trainer.objects.get(pk=trainer_id)
            validated_data['trainer'] = trainer

        return Pokemon.objects.create(**validated_data)

    def update(self, instance, validated_data):

        trainer_id = validated_data.pop('trainer_id', None)
        if trainer_id:
            instance.trainer = Trainer.objects.get(pk=trainer_id)

        return super().update(instance, validated_data)