from mongoengine import *
from mongoengine.django.auth import *
from pacients.models import Pacient
import datetime

class Question(Document):
    name = StringField(max_length=200)
    created = DateTimeField(default=datetime.datetime.now)
    description = StringField(max_length=1200)
    pacient = ReferenceField(Pacient)
    asker = ReferenceField(User)
