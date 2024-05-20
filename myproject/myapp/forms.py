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

class AuteursForm(forms.ModelForm):
    class Meta:
        model = Auteurs
        fields = {'nom','prenom','age','photos'}
        labels = {
            'nom': ("nom de l'auteur"),
            'prenom': ("prenom de l'auteur"),
            'age': ("age de l'auteur"),
            'photos': ("photo de l'auteur")
        }

class CategoriesjeuxForm(forms.ModelForm):
    class Meta:
        model = Categoriesjeux
        fields = {'nom','descriptif'}
        labels = {
            'nom': ('le nom de la catégorie de jeux'),
            'descriptif': ('le descriptif de la catégorie')
        }

class JeuxForm(forms.ModelForm):
    class Meta:
        model = Jeux
        fields = {'titre','anneesortie','photoboite','editeur','auteur','categorie'}
        labels = {
            'titre': ('Titre du jeu'),
            'annesortie':("L'année de sortie du jeu"),
            'photoboite':("Une photo de la boite"),
            'editeur':("l'éditeur du jeu"),
            'auteur': ("l'auteur du jeu"),
            'categorie': ("La catégorie du jeu"),
        }
