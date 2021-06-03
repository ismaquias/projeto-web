from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Post

class Notification(model.Model):
	def send_to_users(self, users):
		pass # enviar para suários

@receiver(post_save, sender=Post)
def post_create_notify(sender, created, *args, **kwargs):
	if created:
		notification = Notification.objects.create()
		notification.send_to_users(users)
