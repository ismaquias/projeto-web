from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from forum import views as forum_views
from authentication import views as auth_views

router = routers.SimpleRouter()
router.register(r'canais', forum_views.CanalViewSet)
router.register(r'comentarios', forum_views.ComentarioViewSet)
router.register(r'posts', forum_views.PostViewSet)
router.register(r'users', auth_views.UserViewSet)

urlpatterns = [
	path('admin/', admin.site.urls),
	path('api/', include(router.urls))
	]