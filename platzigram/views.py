from django.http import HttpResponse

from datetime import datetime

import json
#import pdb

def hello_world(request):
    now = datetime.now().strftime('%b %dth, %Y - %H:%M hrs')
    return HttpResponse(now)

def sorting(request):
    r = sorted([int(i) for i in request.GET['numbers'].split(',')])
    print(r)
    #pdb.set_trace()
    data = {
            'status' : 'ok',
            'numbers' : r,
            'message': 'Ingerers sorted'
            }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request,name,age):
    if age < 12:
        message = f'sorry {name}, you are not allowed here'
    else:
        message = f'Hello, {name}! Welcome to Platzigram'

    return HttpResponse(message)
