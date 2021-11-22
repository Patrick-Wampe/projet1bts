from django.db import models


class Media(models.Model):
    type = models.fields.CharField(max_length=5)
    description = models.fields.CharField(max_length=200, null=True)
    url = models.fields.URLField(max_length=200)


class Instagrameur(models.Model):
    nom = models.fields.CharField(max_length=40)
    pseudo = models.fields.CharField(max_length=40)
    email = models.fields.EmailField(max_length=100)
    mdp = models.fields.CharField(max_length=40)


class Commentaire(models.Model):
    commentaire = models.fields.CharField(max_length=404)
    date = models.fields.DateTimeField(auto_now=True)
    commentateur = models.ForeignKey(Instagrameur, null=True, on_delete = models.SET_NULL)
