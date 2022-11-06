from .views import RestaurantesDelete ,HeladeriasDelete ,BaresDelete, HeladeriasUpdate, RestaurantesUpdate, HeladeriasCreate, RestaurantesCreate, BaresList, BaresDetail, BaresCreate, BaresUpdate, buscar_restaurante, RestaurantesList, HeladeriasList, inicio, buscar_bar, buscar_heladeria
from django.urls import path


urlpatterns = [
    path('', inicio, name="Inicio"),
    path('bares/', BaresList.as_view(), name="Bares"),
    path('bares-detalle/<pk>', BaresDetail.as_view(), name="detalle_bares"),
    path('bares-create/', BaresCreate.as_view(), name="bar_create"),
    path('bares-update/<pk>', BaresUpdate.as_view(), name="bar_update"),
    path('bares-delete/<pk>', BaresDelete.as_view(), name="bar_delete"),
    path('restaurantes/', RestaurantesList.as_view(), name="Restaurantes"),
    path('restaurantes-create/', RestaurantesCreate.as_view(), name="restaurante_create"),
    path('restaurantes-update/<pk>', RestaurantesUpdate.as_view(), name="restaurante_update"),
    path('restaurantes-delete/<pk>', RestaurantesDelete.as_view(), name="restaurante_delete"),
    path('heladerias/', HeladeriasList.as_view(), name="Heladerias"),
    path('heladerias-create/', HeladeriasCreate.as_view(), name="heladeria_create"),
    path('heladerias-update/<pk>', HeladeriasUpdate.as_view(), name="heladeria_update"),
    path('heladerias-delete/<pk>', HeladeriasDelete.as_view(), name="heladeria_delete"),
    path('buscar-restaurante/', buscar_restaurante, name ="buscar_restaurante"),
    path('buscar-bar/', buscar_bar, name ="buscar_bar"),
    path('buscar-heladeria/', buscar_heladeria, name ="buscar_heladeria"),
]