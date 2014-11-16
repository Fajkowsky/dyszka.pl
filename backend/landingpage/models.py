from django.contrib.auth.models import User, UserManager

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
                return {'status': False, 'msg': 'Not all fields are present.'}

        if data['password'] != data['password2']:
            return {'status': False, 'msg': 'Password not equal.'}

        if User.objects.filter(username=data['username']) or User.objects.filter(email=data['email']):
            return {'status': False, 'msg': 'Username or email present in database.'}

        return {'status': True, 'msg': 'Saved.'}