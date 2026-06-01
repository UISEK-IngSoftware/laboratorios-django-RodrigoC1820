import django.urls
from . import views

app_name = 'pokedex'
urlpatterns = [
    django.urls.path('', views.index, name='index'),

    django.urls.path(
        '<int:pokemon_id>/',
        views.pokemon,
        name='pokemon'
    ),

    django.urls.path(
        'trainer/add/',
        views.add_trainer,
        name='add_trainer'
    ),

    django.urls.path(
        'trainer/edit/<int:trainer_id>/',
        views.edit_trainer,
        name='edit_trainer'
    ),

    django.urls.path(
        'trainer/delete/<int:trainer_id>/',
        views.delete_trainer,
        name='delete_trainer'
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
    
    django.urls.path(
        'login/', views.CustomLoginView.as_view(), name='login'
    ),
]
