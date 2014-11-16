from django.views.decorators.csrf import csrf_exempt
from models import Person
from utils import json_response
from json import loads

@csrf_exempt
def user_json(request):
    if request.method == 'GET':
        return json_response({})
    elif request.method == 'POST':
        request_json = loads(request.body)
        msg = Person.validate(**request_json)
        if msg['status']:
            del request_json['password2']
            Person.objects.create_user(**request_json)
        return json_response(msg)
    else:
        return json_response({})
