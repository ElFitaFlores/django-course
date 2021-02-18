from datetime import datetime
from django.http import HttpResponse


def hello_world(request):
    return HttpResponse('Hello world from {now}'.format(
        now=datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    ))


def hi(request):
    return HttpResponse('Hi')


def order_numbers(request):
    numbers = [int(i) for i in request.GET['numbers'].split(',')]
    sorted_numbers = sorted(numbers)
    return HttpResponse(str(sorted_numbers), content_type='application/json')


def say_hi(request, name, age):
    if age < 12:
        message = 'Sorry {} you are not allowed'.format(name)
    else:
        message = 'Hello, {} welcome'.format(name)

    return HttpResponse(message)
