import requests
from django.http import HttpResponse


def home(request: requests.models.Response) -> HttpResponse:
    return HttpResponse('APP is up')
