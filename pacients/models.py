from mongoengine import *
from mongoengine.django.auth import *
import datetime

class Pacient(Document):
    username = StringField(max_length=200)
    birthday = DateTimeField()
    creator = ReferenceField(User)
    created = DateTimeField(default=datetime.datetime.now)
