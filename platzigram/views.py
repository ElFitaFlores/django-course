from datetime import datetime
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello world from {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def hi(request):
    return HttpResponse('Hi')
