from django.test import TestCase, Client
import json


from .models import Url

client = Client()

class ShortenerTest(TestCase):

    def test_make_short_url(self):
        data = {
            "link" : "http://127.0.0.1:8000/api/board/1"
        }

        response = client.post('/shortener/', json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)