from rest_framework import serializers
from .models import Post, Comentario, Canal

class PostSerializer (serializers.ModelSerializer):
	class Meta:
		model = Post
		fields = [ 
		"id", "data_criacao", "user", "canal", "titulo", "texto", "likes", "deslikes"
		]
#		exclude = ["user"]

class ComentarioSerializer (serializers.ModelSerializer):
	class Meta:
		model = Comentario
		fields = "__all__"
#		exclude = ["user"]

class CanalSerializer (serializers.ModelSerializer):
	class Meta:
		model = Canal
		fields = "__all__"
#		exclude = ["user"]