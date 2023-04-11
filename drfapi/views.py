from rest_framework import generics, status, viewsets, mixins
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from .models import Medidor, Medicion

from .serializers import ConsumoTotalSerializer, MedicionSerializer, MedidoresSerializer, ConsumoPromedioSerializer
from .serializers import ConsumoMinimoSerializer, ConsumoMaximoSerializer, MedidorDetalleSerializer, UserSerializer

from .utils import calculo_consumos


'--------------------------------------------- Models ViewSet -------------------------------------------------------'
# Lista de Medidores
class ListaMedidores(viewsets.ReadOnlyModelViewSet):
    queryset = Medidor.objects.all()
    serializer_class = MedidoresSerializer


# Detalles Medidor
class MedidorDetalle(generics.RetrieveAPIView):
    queryset = Medidor.objects.all()
    serializer_class = MedidorDetalleSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), Nombre=self.kwargs['Nombre'])


# Agregar un Medidor
class AgregarMedidor(mixins.CreateModelMixin,
                     viewsets.GenericViewSet):
    serializer_class = MedidoresSerializer

    def perform_create(self, serializer):
        serializer.save(usuario=self.request.user)


# Regsitrar un Consumo
class RegistrarConsumo(mixins.CreateModelMixin,
                       viewsets.GenericViewSet):
    serializer_class = MedicionSerializer

    def perform_create(self, serializer):
        medicion = serializer.save()
        calculo_consumos(medicion.Medidor_id)


# Lista de Mediciones
class ListaMediciones(viewsets.ReadOnlyModelViewSet):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer


# Vista Detalle de Medidicon
class MedicionDetalle(generics.RetrieveAPIView):
    queryset = Medicion.objects.all()
    serializer_class = MedicionSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), pk=self.kwargs['pk'])


# Vista para Mostrar el Cosumo Total
class ConsumoTotal(generics.RetrieveAPIView):
    queryset = Medidor.objects.all()
    serializer_class = ConsumoTotalSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), Nombre=self.kwargs['Nombre'])


# Vista para Mostrar el Cosumo Maximo
class ConsumoMaximo(generics.RetrieveAPIView):
    queryset = Medidor.objects.all()
    serializer_class = ConsumoMaximoSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), Nombre=self.kwargs['Nombre'])


# Vista para Mostrar el Cosumo Minimo
class ConsumoMinimo(generics.RetrieveAPIView):
    queryset = Medidor.objects.all()
    serializer_class = ConsumoMinimoSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), Nombre=self.kwargs['Nombre'])


# Vista para Mostrar el Cosumo Promedio
class ConsumoPromedio(generics.RetrieveAPIView):
    queryset = Medidor.objects.all()
    serializer_class = ConsumoPromedioSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), Nombre=self.kwargs['Nombre'])


# Vista de la lista de Usuarios
class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


# Vista del detalle de un usuario
class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return get_object_or_404(self.get_queryset(), username=self.kwargs['username'])
