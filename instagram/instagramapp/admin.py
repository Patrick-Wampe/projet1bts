from django.contrib import admin

# Register your models here.
from instagramapp.models import Media, Instagrameur, Commentaire

admin.site.register(Media)
admin.site.register(Instagrameur)
admin.site.register(Commentaire)
