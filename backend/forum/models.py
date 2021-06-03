from django.db import models
from django.conf import settings

class Post(models.Model):
	user = models.FogeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	canal = models.FogeignKey ("Canal", on_delete=models.CASCADE)
	data_cracao = models.DateTimeField (auto_now_add=True)
	texto = models.TextField (max_length=255)
	titulo = models.CharField (max_length=255)
	likes = models.BigIntegerField (default=0)
	deslikes = models.BigIntegerField (default=0)
	
	def __str__(self):
		return f"Post <titulo: {self.titulo}>"
		
class Comentario (models.Model):
	user = models.FogeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	post = models.FogeignKey ("Post", on_delete=models.CASCADE)
	data_cracao = models.DateTimeField (auto_now_add=True)
	texto = models.TextField (max_length=255)

	def __str__(self):
		return f"Comentario <{self.id}>"

class Canal (models.Model):
	user = models.FogeignKey (settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
	tema = models.CharField(max_length=255)
	
	def __str__(self):
		return f"Canal <{self.id}>"
