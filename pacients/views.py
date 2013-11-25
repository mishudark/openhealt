import json
from django.http import HttpResponse
from mongoengine.django.auth import *
from pacients.models import Pacient

def list(request):
    items = Pacient.objects()
    response = [{'id': str(i.id),
        'name': i.username
        } for i in items]
    return HttpResponse(json.dumps(response), mimetype='application/json')

def create(request):
    p = Pacient()

    try:
        POST = json.loads(request.body)
    except Exception, e:
        response = {'error': 'invalid data',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    try:
        u = User.objects(username = str(request.user)).first()
        #hack ensure user exist
        u.id
    except Exception, e:
        response = {'error': 'uid no existe',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    name = POST.get('name', None)
    p.username = name
    p.creator = u

    if not name:
        return HttpResponse(json.dumps({'error': 'incompleted data'}), mimetype='application/json')

    p.save()

    return HttpResponse(json.dumps({'id': str(p.id)}), mimetype='application/json')

def update(request):
    try:
        POST = json.loads(request.body)
    except Exception, e:
        response = {'error': 'invalid data',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    pid = POST.get('id', None)
    name = POST.get('name', None)

    if pid:
        try:
            p = Pacient.objects(id = pid).first()
            #hack ensure user exist
            p.id
        except Exception, e:
            response = {'error': 'invalid data',}
            return HttpResponse(json.dumps(response), mimetype='application/json')
    else:
         p = Pacient()

    p.username = name


    if not p.username:
        return HttpResponse(json.dumps({'error': 'data incompleted'}), mimetype='application/json')
    p.save()
    return HttpResponse(json.dumps({'error': '', 'id': str(p.id)}), mimetype='application/json')
