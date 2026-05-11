import django.urls
from . import views

urlpatterns = [
    django.urls.path('', views.index, name='index'),

    django.urls.path(
        '<int:pokemon_id>/',
        views.pokemon,
        name='pokemon'
    ),

    django.urls.path(
        'trainer/<int:trainer_id>/',
        views.trainer_detail,
        name='trainer_details'
    ),

    django.urls.path(
        'pokemon/add/',
        views.add_pokemon,
        name='add_pokemon'
    ),

    django.urls.path(
        'pokemon/edit/<int:pokemon_id>/',
        views.edit_pokemon,
        name='edit_pokemon'
    ),

    django.urls.path(
        'pokemon/delete/<int:pokemon_id>/',
        views.delete_pokemon,
        name='delete_pokemon'
    ),
]