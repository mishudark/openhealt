from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response
from django.middleware.csrf import get_token
from django.http import HttpResponse

from random import randint
import json
import datetime

@login_required
def index(request):
    csrf_token = get_token(request)
    return render_to_response('base.html',
        {'csrf_token': csrf_token})

@login_required
def get_history_day(request):
    if request.method == 'POST':
        data = [{
            'temp': randint(-5,39),
            'wind': randint(3,26),
            'hum': randint(3,100),
            'direction': randint(0,4),
            } for i in range(31)]
        return HttpResponse(json.dumps(data), mimetype='application/json')

    csrf_token = get_token(request)
    return render_to_response('graphics.html',
        {'csrf_token': csrf_token})


@login_required
def get_history(request, day_start, day_end):
    pass
