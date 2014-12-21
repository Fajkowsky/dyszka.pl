from django.contrib.auth.models import User, UserManager
from backend.messages import message
from re import match

fields = (
    'username',
    'email',
    'password',
    'password2'
)


class Person(User):
    objects = UserManager()

    @classmethod
    def validate(cls, **data):
        for field in fields:
            if field not in data:
                return message['not_all_fields']

        if data['password'] != data['password2']:
            return message['not_equal']

        if Person.objects.filter(username=data['username']) or Person.objects.filter(email=data['email']):
            return message['already_in_database']

        if not match('[^@]+@[^@]+\.[^@]+', data['email']):
            return message['not_valid_email']

        del data['password2']
        Person.objects.create_user(**data)
        return message['saved']