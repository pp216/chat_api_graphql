from .models import *
import graphene
from django.contrib.auth.models import User
from graphene_django import DjangoObjectType

class DialogType( DjangoObjectType):
    class Meta:
        model = Dialog


class MessageType( DjangoObjectType):
    class Meta:
        model = Message


class UserType( DjangoObjectType):

    class Meta:
        model = User