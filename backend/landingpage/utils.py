from json import dumps

from django.http import HttpResponse


def json_response(data):
    return HttpResponse(
        dumps(data),
        content_type="application/json"
    )
