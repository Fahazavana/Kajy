from django.contrib import admin
from .models import Post, Commentaire, Vote

# Register your models here.
admin.site.register(Post)
admin.site.register(Commentaire)
admin.site.register(Vote)