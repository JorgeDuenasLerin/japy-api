from rest_framework import serializers
from .models import Atraccion, Bar, Comentario, Actor, Pelicula, Ingrediente, Resultado, Estafado, Criptomoneda, Estafado


class BarSerializer(serializers.HyperlinkedModelSerializer):

   class Meta:
        model = Bar
        fields = '__all__'


class ComentarioSerializer(serializers.HyperlinkedModelSerializer):

   class Meta:
        model = Comentario
        fields = ['texto']


class AtraccionDetailSerializer(serializers.HyperlinkedModelSerializer):
    comentarios=ComentarioSerializer(many=True)

    class Meta:
        model = Atraccion
        fields = ['nombre','descripcion','ocupantes', 'comentarios']


class AtraccionListSerializer(serializers.HyperlinkedModelSerializer):
    #comentarios=ComentarioSerializer(many=True)

    class Meta:
        model = Atraccion
        fields = '__all__'


class ActorSerializer(serializers.HyperlinkedModelSerializer):

   class Meta:
        model = Actor
        fields = '__all__'


class PeliculaDetailSerializer(serializers.HyperlinkedModelSerializer):
    actores=ActorSerializer(many=True)

    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Pelicula
        fields = '__all__'


class PeliculaListRelatedSerializer(serializers.ModelSerializer):
    actores = ActorSerializer(many=True, read_only=True)

    class Meta:
        model = Pelicula
        fields = ['nombre','descripcion', 'estrellas', 'actores']

class HyperlinkedModelSerializerWithId(serializers.HyperlinkedModelSerializer):
    """Extend the HyperlinkedModelSerializer to add IDs as well for the best of
    both worlds.
    """
    id = serializers.ReadOnlyField()


class IngredienteListSerializer(HyperlinkedModelSerializerWithId):

    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'tags')


class IngredienteDetalleSerializer(HyperlinkedModelSerializerWithId):

    class Meta:
        model = Ingrediente
        fields = ('id', 'nombre', 'tags', 'descripcion', 'kcalorias')


class ResultadoListSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Resultado
        fields = '__all__'


class EstafadoSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = Estafado
        fields = ['nombre']
        lookup_field='estafados'


class CriptoSerializer(HyperlinkedModelSerializerWithId):
    estafados = EstafadoSerializer(many=True, read_only=True)

    class Meta:
        model = Criptomoneda
        fields = ['nombre', 'euros', 'estafados']