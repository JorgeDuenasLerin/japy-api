from django.contrib import admin

# Register your models here.
from .models import Atraccion, Bar, Comentario, Pelicula, Actor, Ingrediente, Resultado
from .models import Criptomoneda, Estafado, Cuadro

class ComentarioInline(admin.StackedInline):
    model = Comentario
    extra = 3


class AtraccionAdmin(admin.ModelAdmin):
    model = Atraccion
    inlines = [ComentarioInline]


admin.site.register(Atraccion, AtraccionAdmin)
admin.site.register(Bar)


class ActorInline(admin.StackedInline):
    model = Actor
    extra = 5


class PeliculaAdmin(admin.ModelAdmin):
    model = Pelicula
    inlines = [ActorInline]


admin.site.register(Pelicula, PeliculaAdmin)
admin.site.register(Actor)
admin.site.register(Ingrediente)



class ResultadoAdmin(admin.ModelAdmin):
    model = Resultado


admin.site.register(Resultado, ResultadoAdmin)


class EstafadoInline(admin.StackedInline):
    model = Estafado
    extra = 5


class CriptoAdmin(admin.ModelAdmin):
    model = Criptomoneda
    inlines = [EstafadoInline]


admin.site.register(Criptomoneda, CriptoAdmin)

# registra el cuatro
admin.site.register(Cuadro)

from .models import Destino, ComentarioDestino
admin.site.register(Destino)
admin.site.register(ComentarioDestino)