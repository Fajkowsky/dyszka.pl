from json import loads

from django.views.decorators.csrf import csrf_exempt
from models import Person
from utils import json_response


@csrf_exempt
def register_json(request):
    if request.method == 'POST':
        msg = Person.validate(**loads(request.body))
        return json_response(msg)
    else:
        return json_response({"status": False, "msg": "Not possible."})
