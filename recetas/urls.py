from django.urls import path
from .views import lista_recetas, agregar_receta, eliminar_receta
from . import views


urlpatterns = [
    path('', lista_recetas, name='lista_recetas'),
    path('agregar/', agregar_receta, name='agregar_receta'),
    path('eliminar/<int:id>/', eliminar_receta, name='eliminar_receta'),


]
