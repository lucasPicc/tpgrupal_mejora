from .views import HeladeriasUpdate, RestaurantesUpdate, HeladeriasCreate, RestaurantesCreate, BaresList, BaresDetail, BaresCreate, BaresUpdate, eliminar_bar, buscar_restaurante, RestaurantesList, HeladeriasList, inicio, buscar_bar, buscar_heladeria
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bares/', BaresList.as_view(), name="Bares"),
    path('bares-detalle/<pk>', BaresDetail.as_view(), name="detalle_bares"),
    path('bares-create/', BaresCreate.as_view(), name="bar_create"),
    path('bares-update/<pk>', BaresUpdate.as_view(), name="bar_update"), 
    path('restaurantes/', RestaurantesList.as_view(), name="Restaurantes"),
    path('restaurantes-create/', RestaurantesCreate.as_view(), name="restaurante_create"),
    path('restaurantes-update/<pk>', RestaurantesUpdate.as_view(), name="restaurante_update"), 
    path('heladerias/', HeladeriasList.as_view(), name="Heladerias"),
    path('heladeria-create/', HeladeriasCreate.as_view(), name="heladeria_create"),
    path('heladeria-update/<pk>', HeladeriasUpdate.as_view(), name="heladeria_update"), 
    path('buscar-restaurante/', buscar_restaurante, name ="buscar_restaurante"),
    path('buscar-bar/', buscar_bar, name ="buscar_bar"),
    path('buscar-heladeria/', buscar_heladeria, name ="buscar_heladeria"),
    path('elimina-bar/<int:id>', eliminar_bar, name="eliminaBar"),
]