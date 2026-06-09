from rest_framework import serializers
from pokedex.models import Pokemon, Trainer
from django.core.files.base import ContentFile
import base64

class Base64ImageField(serializers.ImageField):
    def to_internal_value(self, data):
        if isinstance(data, str):
            if data == '' or data is None:
                return None
            if ';base64,' in data:
                try:
                    format, imgstr = data.split(';base64,')
                    ext = format.split('/')[-1]
                    return ContentFile(base64.b64decode(imgstr), name=f'image.{ext}')
                except Exception:
                    raise serializers.ValidationError('La imagen no se encuentra con base64 válida.')
        return super().to_internal_value(data)

class TrainerSerializer(serializers.ModelSerializer):
    photo = Base64ImageField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Trainer
        fields = '__all__'

class PokemonSerializer(serializers.ModelSerializer):
    picture = Base64ImageField(required=False, allow_null=True, use_url=True)

    class Meta:
        model = Pokemon
        fields = '__all__'