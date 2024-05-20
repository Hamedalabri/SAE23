from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Categoriesjeux, Comment, GameList, Jeux , Auteurs
from .forms import PlayerForm, CommentForm, GameListForm , CategoriesjeuxForm , JeuxForm , AuteursForm

User = get_user_model()

# Player CRUD 
@login_required
def create_player(request):
    if request.method == 'POST':
        form = PlayerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm()
    return render(request, 'create_player.html', {'form': form})

@login_required
def player_list(request):
    players = User.objects.all()
    return render(request, 'player_list.html', {'players': players})

@login_required
def update_player(request, pk):
    player = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        form = PlayerForm(request.POST, instance=player)
        if form.is_valid():
            form.save()
            return redirect('player_list')
    else:
        form = PlayerForm(instance=player)
    return render(request, 'update_player.html', {'form': form})

@login_required
def delete_player(request, pk):
    player = get_object_or_404(User, pk=pk)
    if request.method == 'POST':
        player.delete()
        return redirect('player_list')
    return render(request, 'delete_player.html', {'player': player})

# Comment CRUD 
@login_required
def create_comment(request):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm()
    return render(request, 'create_comment.html', {'form': form})

@login_required
def comment_list(request):
    comments = Comment.objects.all()
    return render(request, 'comment_list.html', {'comments': comments})

@login_required
def update_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            return redirect('comment_list')
    else:
        form = CommentForm(instance=comment)
    return render(request, 'update_comment.html', {'form': form})

@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if request.method == 'POST':
        comment.delete()
        return redirect('comment_list')
    return render(request, 'delete_comment.html', {'comment': comment})

# GameList CRUD 
@login_required
def create_game_list(request):
    if request.method == 'POST':
        form = GameListForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('game_list')
    else:
        form = GameListForm()
    return render(request, 'create_game_list.html', {'form': form})

@login_required
def game_list(request):
    game_lists = GameList.objects.all()
    return render(request, 'game_list.html', {'game_lists': game_lists})

@login_required
def update_game_list(request, pk):
    game_list = get_object_or_404(GameList, pk=pk)
    if request.method == 'POST':
        form = GameListForm(request.POST, instance=game_list)
        if form.is_valid():
            form.save()
            return redirect('game_list_list')
    else:
        form = GameListForm(instance=game_list)
    return render(request, 'update_game_list.html', {'form': form})

@login_required
def delete_game_list(request, pk):
    game_list = get_object_or_404(GameList, pk=pk)
    if request.method == 'POST':
        game_list.delete()
        return redirect('game_list_list')
    return render(request, 'delete_game_list.html', {'game_list': game_list})

#CRUD Categorie

def create_categorie(request):
    if request.method == 'POST':
        form = CategoriesjeuxForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('categorie_index')
    else:
        form = CategoriesjeuxForm()
    return render(request, 'create_categorie.html', {'form': form})

def delete_categorie(request, id):
    Categorie = Categoriesjeux.objects.get(pk=id)
    Categorie.delete()
    return HttpResponse("/categorie_index/")

def index_categorie(request):
    liste = Categoriesjeux.objects.all()
    return render(request, 'categorie_index.html',{"liste":liste})

def update_categorie(request, pk):
    categorie = get_object_or_404(Categoriesjeux, pk=pk)
    if request.method == 'POST':
        form = CategoriesjeuxForm(request.POST, instance=categorie)
        if form.is_valid():
            form.save()
            return redirect('index_categorie')
    else:
        form = CategoriesjeuxForm(instance=categorie)
    return render(request, 'update_categorie.html', {'form': form})

#CRUD Jeux

def create_jeux(request):
    if request.method == 'POST':
        form = JeuxForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('jeux_index')
    else:
        form = JeuxForm()
    return render(request, 'create_jeux.html', {'form': form})

def delete_jeux(request, id):
    Jeux = Jeux.objects.get(pk=id)
    Jeux.delete()
    return HttpResponse("/jeux_index/")

def index_jeux(request):
    liste = Jeux.objects.all()
    return render(request, 'jeux_index.html',{"liste":liste})

def update_jeux(request, pk):
    jeux = get_object_or_404(Jeux, pk=pk)
    if request.method == 'POST':
        form = JeuxForm(request.POST, instance=jeux)
        if form.is_valid():
            form.save()
            return redirect('index_jeux')
    else:
        form = JeuxForm(instance=jeux)
    return render(request, 'update_jeux.html', {'form': form})


#CRUD Auteurs

def create_auteurs(request):
    if request.method == 'POST':
        form = AuteursForm (request.POST)
        if form.is_valid():
            form.save()
            return redirect('auteurs_index')
    else:
        form = AuteursForm()
    return render(request, 'create_auteurs.html', {'form': form})

def delete_auteurs(request, id):
    Auteurs = Auteurs.objects.get(pk=id)
    Auteurs.delete()
    return HttpResponse("/auteurs_index/")

def index_auteurs(request):
    liste = Auteurs.objects.all()
    return render(request, 'auteurs_index.html',{"liste":liste})

def update_auteurs(request, pk):
    auteurs = get_object_or_404(Auteurs, pk=pk)
    if request.method == 'POST':
        form = AuteursForm(request.POST, instance=auteurs)
        if form.is_valid():
            form.save()
            return redirect('index_auteurs')
    else:
        form = AuteursForm(instance=auteurs)
    return render(request, 'update_auteurs.html', {'form': form})



def home(request):
    return render(request, 'home.html')
