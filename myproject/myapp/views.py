from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Player, Comment, GameList, Jeux
from .forms import PlayerForm, CommentForm, GameListForm

User = get_user_model()

# Player CRUD operations
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

# Comment CRUD operations
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

# GameList CRUD operations
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
