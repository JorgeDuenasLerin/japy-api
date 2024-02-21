import time
from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import filters
import django_filters.rest_framework

from .models import Bar, Atraccion, Comentario
from .models import Actor, Pelicula, Ingrediente, Resultado
from .serializers import BarSerializer, AtraccionListSerializer, AtraccionDetailSerializer, ComentarioSerializer, ResultadoListSerializer
from .serializers import ActorSerializer, PeliculaDetailSerializer, PeliculaListSerializer, PeliculaListRelatedSerializer
from .serializers import IngredienteListSerializer, IngredienteDetalleSerializer

from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BarViewSet(viewsets.ModelViewSet):
    queryset = Bar.objects.all()
    serializer_class = BarSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    search_fields = ['descripcion']
    filterset_fields = ['estrellas']


class ComentarioViewSet(viewsets.ModelViewSet):
    queryset = Comentario.objects.all()
    serializer_class = ComentarioSerializer


class AtraccionViewSet(viewsets.ModelViewSet):
    queryset = Atraccion.objects.all()
    serializer_class = AtraccionListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return AtraccionDetailSerializer
        else: 
            return AtraccionListSerializer


class ActorViewSet(viewsets.ModelViewSet):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]


class PeliculaViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaListSerializer

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return PeliculaDetailSerializer
        else: 
            return PeliculaListSerializer


class PeliculaRelatedViewSet(viewsets.ModelViewSet):
    queryset = Pelicula.objects.all()
    serializer_class = PeliculaListRelatedSerializer


class IngredienteViewSet(viewsets.ModelViewSet):
    queryset = Ingrediente.objects.all()
    serializer_class = IngredienteListSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['tags']

    def get_queryset(self):
        time.sleep(2)
        return self.queryset

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return IngredienteDetalleSerializer
        else: 
            return IngredienteListSerializer


class ResultadoViewSet(viewsets.ModelViewSet):
    queryset = Resultado.objects.all()
    serializer_class = ResultadoListSerializer