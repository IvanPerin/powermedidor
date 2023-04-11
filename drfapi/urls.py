from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ListaMedidores, AgregarMedidor, RegistrarConsumo, MedidorDetalle, MedicionDetalle, \
    ConsumoTotal, ConsumoPromedio, ConsumoMinimo, ConsumoMaximo, UserList, UserDetail


'------------------------------Create a router and register our viewsets with it------------------------------------'

router = DefaultRouter()
router.register(r'Medidores', ListaMedidores)
router.register(r'Agregar-Medidor', AgregarMedidor, basename="Agregar-Medidor")
router.register(r'Registrar-Consumo', RegistrarConsumo, basename='Registrar_Consumo')


# The API URLs are now determined automatically by the router.
urlpatterns = [
    path(r'', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path('users/', UserList.as_view()),
    path('users/<username>/', UserDetail.as_view(), name='user-detail'),
    path('Medidor/<Nombre>', MedidorDetalle.as_view(), name='medidor-detail'),
    path('Mediciones/<int:pk>', MedicionDetalle.as_view(), name='medicion-detail'),
    path('Medidor/<Nombre>/Consumo-Total/', ConsumoTotal.as_view(), name='consumo-total'),
    path('Medidor/<Nombre>/Consumo-Maximo/', ConsumoMaximo.as_view(), name='consumo-maximo'),
    path('Medidor/<Nombre>/Consumo-Minimo/', ConsumoMinimo.as_view(), name='consumo-minimo'),
    path('Medidor/<Nombre>/Consumo-Promedio/', ConsumoPromedio.as_view(), name='consumo-promedio'),
]

