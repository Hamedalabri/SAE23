from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name='home'),
    #des joueurs
    path('players/create/', views.create_player, name='create_player'),
    path('players/', views.player_list, name='player_list'),
    path('players/<int:pk>/update/', views.update_player, name='update_player'),
    path('players/<int:pk>/delete/', views.delete_player, name='delete_player'),
    #commentaire
    path('comments/create/', views.create_comment, name='create_comment'),
    path('comments/', views.comment_list, name='comment_list'),
    path('comments/<int:pk>/update/', views.update_comment, name='update_comment'),
    path('comments/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    #liste de jeux
    path('game_lists/create/', views.create_game_list, name='create_game_list'),
    path('game_lists/', views.game_list, name='game_list'),
    path('game_lists/<int:pk>/update/', views.update_game_list, name='update_game_list'),
    path('game_lists/<int:pk>/delete/', views.delete_game_list, name='delete_game_list'),

     
    #Categories
    path('categorie/create/', views.create_categorie, name='create_categorie'),
    path('categorie/', views.index_categorie, name='index_categorie'),
    path('categorie/<int:pk>/update/', views.update_categorie, name='update_categorie'),
    path('categorie/<int:pk>/delete/', views.delete_categorie, name='delete_categorie'),
    #Jeux
    path('jeux/create/', views.create_jeux, name='create_jeux'),
    path('jeux/', views.index_jeux, name='index_jeux'),
    path('jeux/<int:pk>/update/', views.update_jeux, name='update_jeux'),
    path('jeux/<int:pk>/delete/', views.delete_jeux, name='delete_jeux'),
    #Auteurs
    path('auteurs/create/', views.create_auteurs, name='create_auteurs'),
    path('auteurs/', views.index_auteurs, name='index_auteurs'),
    path('auteurs/<int:pk>/update/', views.update_auteurs, name='update_auteurs'),
    path('auteurs/<int:pk>/delete/', views.delete_auteurs, name='delete_auteurs'),
]



