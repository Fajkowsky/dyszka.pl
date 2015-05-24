from models.user import User, UserCategory

fixtures = [
    {
        'model': UserCategory,
        'data': [
            {
                'name': 'admin'
            },
            {
                'name': 'user'
            }
        ]
    },
    {
        'model': User,
        'data': {
            'email': 'admin@dyszka.pl',
            'username': 'admin',
            'password': 'a',
            'active': 1,
            'category_id': 1
        }
    }
]
