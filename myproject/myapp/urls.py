from django.urls import path
from .views import create_player, player_list, update_player, delete_player, create_comment, comment_list, update_comment, delete_comment, create_game_list, game_list, update_game_list, delete_game_list

urlpatterns = [
    #des joueurs
    path('players/create/', create_player, name='create_player'),
    path('players/', player_list, name='player_list'),
    path('players/<int:pk>/update/', update_player, name='update_player'),
    path('players/<int:pk>/delete/', delete_player, name='delete_player'),
    #commentaire
    path('comments/create/', create_comment, name='create_comment'),
    path('comments/', comment_list, name='comment_list'),
    path('comments/<int:pk>/update/', update_comment, name='update_comment'),
    path('comments/<int:pk>/delete/', delete_comment, name='delete_comment'),
    #liste de jeux
    path('game_lists/create/', create_game_list, name='create_game_list'),
    path('game_lists/', game_list, name='game_list'),
    path('game_lists/<int:pk>/update/', update_game_list, name='update_game_list'),
    path('game_lists/<int:pk>/delete/', delete_game_list, name='delete_game_list'),
]