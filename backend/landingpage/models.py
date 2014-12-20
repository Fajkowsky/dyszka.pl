from django.contrib.auth.models import User, UserManager
from backend.messages import message

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
            return {'status': False, 'msg': 'Password not equal.'}

        if Person.objects.filter(username=data['username']) or Person.objects.filter(email=data['email']):
            return {'status': False, 'msg': 'Username or email present in database.'}

        del data['password2']
        Person.objects.create_user(**data)
        return {'status': True, 'msg': 'Saved.'}