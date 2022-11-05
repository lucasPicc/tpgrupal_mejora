from .views import editar_bar, eliminar_bar, buscar_restaurante, heladeria_formulario, BaresList, RestaurantesList, HeladeriasList, inicio, bar_formulario, restaurante_formulario, buscar_bar, buscar_heladeria
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bares', BaresList.as_view(), name="Bares"),
    path('bar-formulario/', bar_formulario, name="bar_formulario"),
    path('restaurantes/', RestaurantesList.as_view(), name="Restaurantes"),
    path('restaurante-formulario/', restaurante_formulario, name="restaurante_formulario"),
    path('heladerias/', HeladeriasList.as_view(), name="Heladerias"),
    path('heladeria-formulario/', heladeria_formulario, name="heladeria_formulario"),
    path('buscar-restaurante/', buscar_restaurante, name ="buscar_restaurante"),
    path('buscar-bar/', buscar_bar, name ="buscar_bar"),
    path('buscar-heladeria/', buscar_heladeria, name ="buscar_heladeria"),
    path('elimina-bar/<int:id>', eliminar_bar, name="eliminaBar"),
    path('editar-bar/<int:id>', editar_bar, name="editaBar"), 
]