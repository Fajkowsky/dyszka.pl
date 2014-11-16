from json import loads

from django.views.decorators.csrf import csrf_exempt
from models import Person
from utils import json_response


@csrf_exempt
def register_json(request):
    if request.method == 'POST':
        request_json = loads(request.body)
        msg = Person.validate(**request_json)
        if msg['status']:
            del request_json['password2']
            Person.objects.create_user(**request_json)
        return json_response(msg)
    else:
        return json_response({"msg": "Not possible."})
