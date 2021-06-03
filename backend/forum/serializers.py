from rest_framework import serializers
from forum.models import Post, Comentario, Canal

class PostSerializer (serializers.HyperlinkModelSerializer):
	class Meta:
		model = Post
		fields = [ 
		"id", "data_criacao", "user", "canal", "titulo", "testo", "likes", "deslikes"
		]
#		exclude = ["user"]

class ComentarioSerializer (serializers.HyperlinkModelSerializer):
	class Meta:
		model = Comentario
		fields = "__all__"
#		exclude = ["user"]

class CanalSerializer (serializers.HyperlinkModelSerializer):
	class Meta:
		model = Canal
		fields = "__all__"
#		exclude = ["user"]