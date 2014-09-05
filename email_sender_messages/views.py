from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello there!")


def detail(request, message_id):
    return HttpResponse("Message id {}".format(message_id))
