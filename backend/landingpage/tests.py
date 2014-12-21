from json import dumps

from django.test import TestCase, Client
from backend.messages import message
from models import Person


class ResponseTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.bad_user = {
            'username': 'username',
            'email': 'emailemail.com',
            'password': 'password',
            'password2': 'password2'
        }
        self.good_user = {
            'username': 'username',
            'email': 'email@email.com',
            'password': 'password',
            'password2': 'password'
        }

    def test_dummy(self):
        self.assertTrue(2+2)

    def test_get_response(self):
        response = self.client.get('/register/')
        self.assertEqual(response.content, dumps(message['not_possible']))

    def test_post_response_no_data(self):
        response = self.client.post('/register/', content_type='application/json')
        self.assertEqual(response.content, dumps(message['not_all_fields']))

    def test_post_response_not_equal_emails(self):
        response = self.client.post('/register/', data=dumps(self.bad_user), content_type='application/json')
        self.assertEqual(response.content, dumps(message['not_equal']))

    def test_post_response_user_already_in_database(self):
        Person(
            username=self.good_user['username'],
            email=self.good_user['email'],
            password=self.good_user['password']
        ).save()

        response = self.client.post('/register/', data=dumps(self.good_user), content_type='application/json')
        self.assertEqual(response.content, dumps(message['already_in_database']))

    def test_post_response_user_saved(self):
        response = self.client.post('/register/', data=dumps(self.good_user), content_type='application/json')
        self.assertEqual(response.content, dumps(message['saved']))

    def test_post_response_not_valid_email(self):
        bad_user = self.bad_user
        bad_user['password2'] = self.bad_user['password']
        print(self.bad_user)
        response = self.client.post('/register/', data=dumps(bad_user), content_type='application/json')
        self.assertEqual(response.content, dumps(message['not_valid_email']))