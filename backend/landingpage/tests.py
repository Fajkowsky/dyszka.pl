from json import dumps

from django.test import TestCase, Client
from backend.messages import message


class ResponseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = {
            'username': 'username',
            'email': 'email@email.com',
            'password': 'password',
            'password2': 'password2'
        }

    def test_get_response(self):
        response = self.client.get('/register/')
        self.assertEqual(response.content, dumps(message['not_possible']))

    def test_post_response_no_data(self):
        response = self.client.post('/register/', content_type='application/json')
        self.assertEqual(response.content, dumps(message['not_all_fields']))

    def test_post_response_not_equal(self):
        response = self.client.post('/register/', data=dumps(self.user), content_type='application/json')
        self.assertEqual(response.content, dumps(message['not_equal']))
