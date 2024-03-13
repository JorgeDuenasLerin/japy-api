from django.db import models

class Bar(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    cierre = models.DateTimeField('Cierre')
    apertura = models.DateTimeField('Apertura')
    estrellas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Atraccion(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    ocupantes = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Comentario(models.Model):
    atraccion = models.ForeignKey(Atraccion, on_delete=models.CASCADE, related_name='comentarios')
    texto = models.CharField(max_length=200)
    
    def __str__(self):
        return self.texto


class Pelicula(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    estrellas = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Actor(models.Model):
    pelicula = models.ForeignKey(Pelicula, on_delete=models.CASCADE, related_name='actores')
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


class Ingrediente(models.Model):
    nombre = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200)
    tags = models.CharField(max_length=255)
    kcalorias = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Resultado(models.Model):
    nombre = models.CharField(max_length=200)
    localidad = models.CharField(max_length=200)
    fecha = models.DateTimeField('Conseguido')
    centimetros = models.IntegerField(default=0)

    def __str__(self):
        return self.nombre


class Criptomoneda(models.Model):
    nombre = models.CharField(max_length=200)
    euros = models.FloatField(default=0)

    def __str__(self):
        return self.nombre


class Estafado(models.Model):
    cripto = models.ForeignKey(Criptomoneda, on_delete=models.CASCADE, related_name='estafados')
    nombre = models.CharField(max_length=200)
    
    def __str__(self):
        return self.nombre


# Un modelo django para almacenar cuadros de arte con nombre del cuadro, precio, fecha de creación y técnica
class Cuadro(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.FloatField(default=0)
    fecha = models.DateTimeField('Creado')
    tecnica = models.CharField(max_length=200)
    color = models.CharField(max_length=200)

    def __str__(self):
        return self.nombre