import json
from django.http import HttpResponse
from mongoengine.django.auth import *
from poll.models import Poll

def create(request):

    POST = false
    try:
        POST = json.loads(request.body)
    except Exception, e:
        response = {'error': 'invalid data',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    if not POST:
        response = {'error': 'invalid data',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    try:
        u = User.objects(username = str(request.user)).first()
        #hack ensure user exist
        u.id
    except Exception, e:
        response = {'error': 'uid no existe',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    p = Poll()
    p.data = json.dumps(POST.get('data', '')
    p.title = POST.get('title', '')
    p.creator = u
    p.save()
