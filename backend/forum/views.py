from rest_framework import viewsets
from .serializers import PostSerializer, ComentarioSerializer, CanalSerializer

from .models import Canal, Comentario, Post

class CanalViewSet(viewsets.ModelViewSet):
	queryset = Canal.objects.all()
	serializer_class = CanalSerializer
	
class ComentarioViewSet(viewsets.ModelViewSet):
	queryset = Comentario.objects.all()
	serializer_class = ComentarioSerializer

class PostViewSet(viewsets.ModelViewSet):
	#queryset = Post.objects.filter(titulo="xyz")
	queryset = Post.objects.all()
	serializer_class = PostSerializer
