from json import dumps

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


@csrf_exempt
def user_json(request):
    if request.method == 'GET':
        return HttpResponse(
            dumps({"status": "GET"}),
            content_type="application/json"
        )
    elif request.method == 'POST':
        return HttpResponse(
            dumps({"status": "POST"}),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            dumps({"status": "ELSE"}),
            content_type="application/json"
        )
