from django import forms
from .models import Categoriesjeux, Jeux, Auteurs, Player, Comment, GameList
from django.contrib.auth.forms import UserCreationForm

class PlayerForm(UserCreationForm):
    class Meta:
        model = Player
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2', 'type']

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['jeu', 'joueur', 'note', 'commentaire']

class GameListForm(forms.ModelForm):
    class Meta:
        model = GameList
        fields = ['joueur', 'jeu']