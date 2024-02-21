from rest_framework import routers
from django.urls import path, include
from .views import BarViewSet, AtraccionViewSet, ComentarioViewSet, PeliculaViewSet, ActorViewSet, IngredienteViewSet, ResultadoViewSet, PeliculaRelatedViewSet


router = routers.DefaultRouter()
router.register(r'bares', BarViewSet)
router.register(r'atracciones', AtraccionViewSet)
router.register(r'comentarios', ComentarioViewSet)
router.register(r'peliculas', PeliculaViewSet)
router.register(r'actores', ActorViewSet)
router.register(r'ingrediente', IngredienteViewSet)
router.register(r'resultado', ResultadoViewSet)
router.register(r'peliculas_related', PeliculaRelatedViewSet)


from . import views

urlpatterns = [
    path('', include(router.urls)),
]