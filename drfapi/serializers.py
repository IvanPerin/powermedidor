from rest_framework import serializers
from .models import Medidor, Medicion


# Serializador para la lista de Medidores
class MedidoresSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Medidor
        fields = ['Nombre', 'Llave_Ident', 'url']
        extra_kwargs = {
            'url': {'lookup_field': 'Nombre'}
                        }


# Serializador para los detalles del Medidor
class MedidorDetalleSerializer(serializers.HyperlinkedModelSerializer):
    Mediciones = serializers.HyperlinkedRelatedField(many=True, read_only=True, view_name='medicion-detail')
    Consumo_Total = serializers.HyperlinkedIdentityField(view_name='consumo-total', lookup_field='Nombre')
    Consumo_Maximo = serializers.HyperlinkedIdentityField(view_name='consumo-maximo', lookup_field='Nombre')
    Consumo_Minimo = serializers.HyperlinkedIdentityField(view_name='consumo-minimo', lookup_field='Nombre')
    Consumo_Promedio = serializers.HyperlinkedIdentityField(view_name='consumo-promedio', lookup_field='Nombre')

    class Meta:
        model = Medidor
        fields = ['Nombre', 'Llave_Ident', 'Mediciones', 'Consumo_Total', 'Consumo_Maximo', 'Consumo_Minimo',
                  'Consumo_Promedio']


# Serializador para Agregar Medidor
class AgregarMedidorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ['Nombre']


# Serializador para las Mediciones
class MedicionSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Medicion
        fields = ['url', 'Medidor', 'Consumo', 'Fecha_hora']


# Serializador para obtener el Consumo Total
class ConsumoTotalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ['Nombre', 'Llave_Ident', 'Consumo_total']


# Serializador para obtener el Consumo Promedio
class ConsumoPromedioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ['Nombre', 'Llave_Ident', 'Consumo_prom']


# Serializador para obtener el Consumo Minimo
class ConsumoMinimoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ['Nombre', 'Llave_Ident', 'Consumo_min']


# Serializador para obtener el Consumo Maximo
class ConsumoMaximoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medidor
        fields = ['Nombre', 'Llave_Ident', 'Consumo_max']
