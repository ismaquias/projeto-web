from django.test import TestCase
from django.test import Client
from django.test import reverse_lazy
from django.contrib.auth import get_user_model

from backend.forum.models import Canal, Comentario, Post

User = get_user_model()

class PostRouteTest (TestCase):
	def setUpClass(self):
		pass
	def setUp(self):
		self.client = Client()
		self.headers = {'Content-Type': 'application/json', 'Accept-Encoding': None}
		self.user = User.objects.create(username="teste", password="teste", email="test@mail.com")
		self.canal = Canal.objects.create(user=self.user, tema="Ciência da Computação"))
		
	def tearDown(self):
		pass
	def tearDownClass(self):
		pass
		
	def test_list_posts (self):
		url = reverse_lazy("post-list")
		response = self.client.get(url)
		self.assertEqual(response.json(),[])
		
	def test_create_post_success(self):
		data = {
			"user": self.user.id,
			"canal": self.canal.id,
			"likes": 0,
			"deslikes": 0,
			"titulo": "Post criado comtestes",
			"texto": "adasd"
		}
		url = reverse_lazy("post-list")  
		response = self.client.post (url, data=data)
#		print(response.json(), response.status_code)
		self.assertEqual(response.status_code, 201)
