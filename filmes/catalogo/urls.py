# catalogo/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('filmes/', views.FilmeList.as_view()),
    path('filmes/<int:pk>/', views.FilmeDetail.as_view()),
    path('filmes/genero/<str:genero>/', views.FilmeByGenero.as_view()),
]