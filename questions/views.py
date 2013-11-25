import json
from django.http import HttpResponse
from questions.models import Question
from pacients.models import Pacient
from mongoengine.django.auth import *

def list(request):
    try:
        POST = json.loads(request.body)
    except Exception, e:
        response = [];
        return HttpResponse(json.dumps(response), mimetype='application/json')

    items = Question.objects(pacient=POST.get('uid',0)).order_by('created')
    print items
    response = [{'id': str(i.id),
        'text': i.name,
        'description': i.description
        } for i in items]

    return HttpResponse(json.dumps(response), mimetype='application/json')

def create(request):
    p = Question()
    p.save()

    return HttpResponse(json.dumps({'id': str(p.id)}), mimetype='application/json')

def update(request):
    p = Question()

    try:
        POST = json.loads(request.body)
    except Exception, e:
        response = {'error': 'invalid data',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    aid = POST.get('id', None)

    try:
        u = User.objects(username = str(request.user)).first()
        pacient = Pacient.objects(id = POST.get('pid','')).first()
        #hack ensure user exist
        u.id
        pacient.id

        if aid:
            p = Question.objects(id = aid).first()
            p.id
    except Exception, e:
        response = {'error': 'invalid data id',}
        return HttpResponse(json.dumps(response), mimetype='application/json')

    p.name = POST.get('text', None)
    p.description = POST.get('description', None)
    p.asker = u
    p.pacient = pacient

    if not p.name or not p.description:
        return HttpResponse(json.dumps({'error': 'data incompleted'}), mimetype='application/json')
    p.save()
    return HttpResponse(json.dumps({'error': '', 'id': str(p.id)}), mimetype='application/json')
