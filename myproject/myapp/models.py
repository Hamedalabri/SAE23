from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.



class Player(AbstractUser):
    TYPE_CHOICES = [
        ('professionnel', 'Professionnel'),
        ('particulier', 'Particulier'),
    ]
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


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