from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Auteurs(models.Model):
    nom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    age = models.IntegerField()
    photos = models.ImageField()

    def __str__(self):
        return f"vous avez ajouter un auteur au nom de {self.nom} {self.prenom}"
    

class Categoriesjeux(models.Model):
    nom = models.CharField(max_length=100)
    descriptif = models.TextField(null = True, blank = True)
    
    def __str__(self):
        return f"Vous avez ajouter une catégorie de jeux au nom {self.nom}"
    
class Jeux(models.Model):
    titre = models.CharField(max_length=200)
    anneesortie = models.DateField()
    photoboite = models.ImageField()
    editeur = models.CharField(max_length= 200)
    auteur = models.ForeignKey(Auteurs, on_delete=models.CASCADE)
    categorie = models.ForeignKey(Categoriesjeux, on_delete=models.CASCADE)

    def __str__(self):
        return f"Vous avez ajouter un  jeux au nom de {self.titre} edité par {self.editeur}"




class Player(AbstractUser):
    type = models.CharField(max_length=20, choices=[('user', 'User'), ('admin', 'Admin')])
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='player_set',  # Change to avoid clash
        blank=True,
        help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',
        related_query_name='player'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='player_permissions_set',  # Change to avoid clash
        blank=True,
        help_text='Specific permissions for this user.',
        related_query_name='player'
    )


class Comment(models.Model):
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)
    joueur = models.ForeignKey(Player, on_delete=models.CASCADE)
    note = models.IntegerField()
    commentaire = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Commentaire de {self.joueur.username} sur {self.jeu.titre}"



class GameList(models.Model):
    joueur = models.ForeignKey(Player, on_delete=models.CASCADE)
    jeu = models.ForeignKey(Jeux, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('joueur', 'jeu')

    def __str__(self):
        return f"la liste de {self.joueur.username} a {self.jeu.titre}"
    

    

       