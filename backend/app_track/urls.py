from django.urls import path
from . import views

urlpatterns = [
    path('personne/', views.PersonneList.as_view()),
    path('', views.all_personne, name='all_personne'),
    path('create', views.create_personne, name='create_prsonne')
]