from django.db import models
import uuid

# Create your models here.


class Medidor(models.Model):

    Llave_Ident = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Nombre = models.CharField(max_length=20)
    Consumo_max = models.FloatField(default=0.0)
    Consumo_min = models.FloatField(default=0.0)
    Consumo_total = models.FloatField(default=0.0)
    Consumo_prom = models.FloatField(default=0.0)

    class Meta:
        ordering = ['Nombre']

    def __str__(self):
        return self.Nombre


class Medicion(models.Model):
    Medidor = models.ForeignKey(Medidor, on_delete=models.SET_NULL, null=True,
                                related_name='Mediciones')
    # related_name es el nombre que debe tener el campo que se agregue en el serializador para relacionar los modelos
    Consumo = models.FloatField(default=0.0)
    Fecha_hora = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Medidor.Nombre + f"\t - \tConsumo: {self.Consumo}"
