from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('crear_libro', views.crear_libro, name="crear_libro"),
    path('books/<int:id>', views.ver_libro, name='ver_libro'),
    path('books/agregar_autor/<int:id>', views.agregar_autor, name='agregar_autor'),
    path('authors', views.index_authors, name="index_authors"),
    path('crear_autor', views.crear_autor, name="create_auhtor"),
    path('authors/<int:id>', views.ver_autor, name="ver_autor"),
    path('authors/agregar_libro/<int:id>', views.agregar_libro, name="agregar_libro"),
]