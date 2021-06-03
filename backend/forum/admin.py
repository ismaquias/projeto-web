from django.contrib import admin
from .models import Post, Comentario, Canal

admin.site.register(Canal)
admin.site.register(Comentario)
admin.site.register(Post)
